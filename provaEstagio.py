from tkinter import * 

import sqlite3

root = Tk()
root.title('LDXPS')

#Create a db or connection to one
conn = sqlite3.connect('cadastro.db')
#Create cursor
c = conn.cursor()

""""

c.execute('''CREATE TABLE VENDEDORES(

	CDVEND varchar(36),
	DSNOME varchar(50),
	CDTAB INTEGER,
	DTNASC DATE,
	PRIMARY KEY (CDVEND)
	)'''
	)


c.execute('''CREATE TABLE CLIENTES(


	CDCL VARCHAR(36) PRIMARY KEY,
	DSNOME VARCHAR(50),
	IDTIPO CHAR(2),
	FOREIGN KEY (DSNOME) REFERENCES vendedores(CDVEND),
	DSLIM DECIMAL(15,2)
	)'''
	)

"""

def edit():
	editor = Tk()
	editor.title('Atualizar Cadastro')

	conn = sqlite3.connect('cadastro.db')
	#Create cursor
	c = conn.cursor()
	record_id = delete_box.get()
	record_id1=delete_box.get()


	#Query the database
	c.execute('SELECT * FROM VENDEDORES WHERE oid = ' +  record_id)
	c.execute('SELECT * FROM CLIENTES WHERE oid = ' +  record_id1)
	records = c.fetchall()
	#Create Global Variables for text box names
	global vend_tx_editor
	global nome_tx_editor
	global cdTab_tx_editor
	global dtNasc_tx_editor
	global CDCL_tx_editor
	global DSNOME_tx_editor
	global IDTIPO_tx_editor
	global DSLIM_tx_editor
	#Create Text Boxes
	vend_tx_editor = Entry(editor,width=30)
	vend_tx_editor.grid(row=0, column=1, padx=20 )
	nome_tx_editor = Entry(editor,width=30)
	nome_tx_editor.grid(row=1, column=1, padx=20 )
	cdTab_tx_editor = Entry(editor,width=30)
	cdTab_tx_editor.grid(row=2, column=1, padx=20 )
	dtNasc_tx_editor = Entry(editor,width=30)
	dtNasc_tx_editor.grid(row=3, column=1, padx=20 )
	CDCL_tx_editor=Entry(editor,width=30)
	CDCL_tx_editor.grid(row=4, column=1, padx=20 )
	DSNOME_tx_editor=Entry(editor,width=30)
	DSNOME_tx_editor.grid(row=5, column=1, padx=20 )
	IDTIPO_tx_editor=Entry(editor,width=30)
	IDTIPO_tx_editor.grid(row=6, column=1, padx=20 )
	DSLIM_tx_editor=Entry(editor,width=30)
	DSLIM_tx_editor.grid(row=7, column=1, padx=20 )

	
	#Create Text Box Labels
	vend_label_editor = Label(editor, text="Códido do Vendedor")
	vend_label_editor.grid(row=0, column=0)
	nome_label_editor = Label(editor, text="Nome")
	nome_label_editor.grid(row=1, column=0)
	cod_label_editor = Label(editor, text="Código de Tabela")
	cod_label_editor.grid(row=2, column=0)
	dtNas_label_editor = Label(editor, text="Data de Nascimento")
	dtNas_label_editor.grid(row=3, column=0)
	CDCL_label_editor=Label(editor, text='Código do cliente')
	CDCL_label_editor.grid(row=4, column=0)
	DSNOME_label_editor=Label(editor, text='Nome do cliente')
	DSNOME_label_editor.grid(row=5, column=0)
	IDTIPO_label_editor=Label(editor, text='Tipo de cliente')
	IDTIPO_label_editor.grid(row=6, column=0)
	DSLIM_label_editor=Label(editor, text='Limite do cliente')
	DSLIM_label_editor.grid(row=7, column=0)

	for record in records:
		vend_tx_editor.insert(0, record[0])
		nome_tx_editor.insert(0, record[1])
		cdTab_tx_editor.insert(0, record[2])
		dtNasc_tx_editor.insert(0, record[3])
		CDCL_tx_editor.insert(0, record[4])
		DSNOME_tx_editor.insert(0, record[5])
		IDTIPO_tx_editor.insert(0, record[6])
		DSLIM_tx_editor.insert(0, record[7])

	update_btn = Button(editor, text='Save record', command=update)
	update_btn.grid(row=20, column=0, columnspan=2, pady=10, padx=10,ipadx=137)

	#Commit Changes
	conn.commit()
	#Close Connection
	conn.close()




	
#Create Submit Function for database
def submit():
	#Create a db or connection to one
	conn = sqlite3.connect('cadastro.db')
	#Create cursor
	c = conn.cursor()
	#Insert Into Table
	

	c.execute('INSERT INTO VENDEDORES VALUES(:vend_tx, :nome_tx, :cdTab_tx, :dtNasc_tx)',

			{
				'vend_tx': vend_tx.get(),
				'nome_tx': nome_tx.get(),
				'cdTab_tx': cdTab_tx.get(),
				'dtNasc_tx': dtNasc_tx.get()

			}

		)
	c.execute('INSERT INTO CLIENTES VALUES(:cdCl_tx, :nomeCl_tx, :idTipo_tx, :dsLim_tx)',
			{
				'cdCl_tx':cdCl_tx.get(),
				'nomeCl_tx':nomeCl_tx.get(),
				'idTipo_tx':idTipo_tx.get(),								
				'dsLim_tx':dsLim_tx.get()


			}
		)
	#Commit Changes
	conn.commit()
	#Close Connection
	conn.close()



def update():

	#Create a db or connection to one
	conn = sqlite3.connect('cadastro.db')
	#Create cursor
	c = conn.cursor()
	record_id = delete_box.get()
	record_id1=delete_box.get()

	c.execute('''UPDATE VENDEDORES SET
		CDVEND = :CD,
		DSNOME = :NOME,
		CDTAB = :COD,
		DTNASC = :NAS
		
		WHERE oid = :oid''',
		{
		'CD':cdTab_tx_editor.get(),
		'NOME': nome_tx_editor.get(),
		'COD': cdTab_tx_editor.get(),
		'NAS': dtNasc_tx_editor.get(),
		

		'oid': record_id

		}
		)



		
	c.execute('''UPDATE CLIENTES SET
		CDCL = :CL,
		DSNOME = :NOMECL,
		IDTIPO = :TIPOCL,
		DSLIM = :LIMCL

		WHERE oid = :oid''',
		{
		'CL':CDCL_tx_editor.get(),
		'NOMECL':nome_tx_editor.get(),
		'TIPOCL': IDTIPO_tx_editor.get(),
		'LIMCL': DSLIM_tx_editor.get(),

		'oid': record_id1
		}
		)


	#Commit Changes
	conn.commit()
	#Close Connection
	conn.close()

	vend_tx.delete(0,END)
	nome_tx.delete(0,END)
	cdTab_tx.delete(0,END)
	dtNasc_tx.delete(0,END)


def query():
	#Create a db or connection to one
	conn = sqlite3.connect('cadastro.db')
	#Create cursor
	c = conn.cursor()

	#Query the database
	c.execute('SELECT *, oid FROM VENDEDORES')
	c.execute('SELECT *, oid FROM CLIENTES')
	records = c.fetchall()
	#print(records)
	print_records = ''
	for record in records:
		print_records += str(record) + '\n'

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2, pady=10,padx=10,ipadx=137)




	conn.commit()
	#Close Connection
	conn.close()

def delete():
	#Create a db or connection to one
	conn = sqlite3.connect('cadastro.db')
	#Create cursor
	c = conn.cursor()

	#Delete a record
	c.execute('DELETE FROM VENDEDORES WHERE oid = ' + delete_box.get())
	delete_box.delete(0,END)

	conn.commit()
	#Close Connection
	conn.close()


#Create Text Boxes
vend_tx = Entry(root,width=30)
vend_tx.grid(row=0, column=1, padx=20 )
nome_tx = Entry(root,width=30)
nome_tx.grid(row=1, column=1, padx=20 )
cdTab_tx = Entry(root,width=30)
cdTab_tx.grid(row=2, column=1, padx=20 )
dtNasc_tx = Entry(root,width=30)
dtNasc_tx.grid(row=3, column=1, padx=20 )
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

#Create Text Box Labels
vend_label = Label(root, text="Códido do Vendedor")
vend_label.grid(row=0, column=0)
vend_label = Label(root, text="Nome")
vend_label.grid(row=1, column=0)
vend_label = Label(root, text="Código de Tabela")
vend_label.grid(row=2, column=0)
vend_label = Label(root, text="Data de Nascimento")
vend_label.grid(row=3, column=0)
delete_box_label = Label(root, text='Selecionar ID do vendedor')
delete_box_label.grid(row=9, column=0, pady=5)

#Create Submit Button

submit_btn = Button(root, text='Criar vendedor', command = submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=145)

#Create a Query Button
query_btn = Button(root, text='Mostrar vendedor', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10,ipadx=160)

#Create a Delete Button
delete_btn = Button(root, text='Excluir vendedor', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10,ipadx=145)

#Create an Update Button
update_btn = Button(root, text='Editar vendedor', command=edit)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10,ipadx=149)


conn.commit()

conn.close()

root.mainloop()