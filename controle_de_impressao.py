import ldap
import Pmw
from Tkinter import *


class Sistema:
   def __init__(self,raiz):
     # Create the ScrolledListBox.
     self.box = Pmw.ScrolledListBox(raiz,labelpos='nw',label_text='Lista de Impressao',listbox_height = 6,selectioncommand=self.login,usehullsize = 1,hull_width = 400,hull_height = 300,)

	
     self.box.pack(fill = 'both', expand = 1, padx = 5, pady = 5)
     for a in range(1,50):
        self.box.insert('end','10:40:01 - Clodonil Trigo')
        
    
   
   def check_credentials(self):
     username = self.nome.get()
     password = self.senha.get()
     LDAP_SERVER = 'ldap://172.16.0.18'
     # fully qualified AD user name
     LDAP_USERNAME = '%s@KEEPERSBRASIL.COM' % username
     # your password
     LDAP_PASSWORD = password
     base_dn = 'DC=KEEPERSBRASIL,DC=COM'
     ldap_filter = 'userPrincipalName=%s@KEEPERSBRASIL.COM' % username
     attrs = ['memberOf']
     try:
         # build a client
         ldap_client = ldap.initialize(LDAP_SERVER)
         # perform a synchronous bind
         ldap_client.set_option(ldap.OPT_REFERRALS,0)
         ldap_client.simple_bind_s(LDAP_USERNAME, LDAP_PASSWORD)
     except ldap.INVALID_CREDENTIALS:
         ldap_client.unbind()
         self.msg['text']='Senha incorreta!'
         return False
     except ldap.SERVER_DOWN:
         self.msg['text']='Senha incorreta!'
         return False
     # all is well
     # get all user groups and store it in cerrypy session for future use
     # cherrypy.session[username] = str(ldap_client.search_s(base_dn,ldap.SCOPE_SUBTREE, ldap_filter, attrs)[0][1]['memberOf'])
     #print str(ldap_client.search_s(base_dn,ldap.SCOPE_SUBTREE, ldap_filter, attrs)[0])
     ldap_client.unbind()
     self.raiz.destroy()
     return True 


         
   def login(self):
      sels = self.box.getcurselection()
      if len(sels) != 0:

         self.raiz = Tk()
         self.raiz.title('Sistema de Impressao - Autenticao')

         self.impressao= Frame(self.raiz)
         self.impressao.pack()
         Label(self.impressao,text=sels[0]).grid(row=1, column=1,sticky=W, pady=3)

         self.login = Frame(self.raiz)
         self.login.pack()
         
         
         Label(self.login,text='Nome:').grid(row=1, column=1,sticky=W, pady=3)
         Label(self.login,text='Senha:').grid(row=2, column=1,sticky=W, pady=3)
         self.msg=Label(self.login,text='')
         self.msg.grid(row=3, column=1, columnspan=2)
         self.nome=Entry(self.login, width=10)
         self.nome.grid(row=1, column=2, sticky=E+W, pady=3)
         self.nome.focus_force()
         self.senha=Entry(self.login, width=5, fg='darkgray',show='l',font=('Wingdings','10'))
         self.senha.grid(row=2,column=2, sticky=E+W, pady=3)
         self.ok=Button(self.login, width=8, command=self.check_credentials,text='OK')
         self.ok.grid(row=4, column=1, padx=2, pady=3)
         self.close=Button(self.login, width=8, command=self.fechar,text='Fechar')
         self.close.grid(row=4, column=2, padx=2, pady=3)


   def fechar(self): self.raiz.destroy()


inst1=Tk()
inst1.title("Controle de Impressao")
Sistema(inst1)
exitButton = Button(inst1, text = 'Exit', command = inst1.destroy)
exitButton.pack(side = 'bottom')
inst1.mainloop()
