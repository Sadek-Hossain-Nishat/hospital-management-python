from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):

        self.root = root
        self.root.title('+Hospital Management System')
        self.root.geometry('1540x800+0+0')

        self.Nameoftablets = StringVar()
        self.NumberofTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.Number = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedicine = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatinetName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        lbltitle = Label(self.root,
                         bd=20, relief=RIDGE,
                         text="HOSPITAL MANAGEMENT SYSTEM",
                         fg='red',
                         bg='white',
                         font=('times new roman',
                               50,
                               'bold'))
        lbltitle.pack(side=TOP, fill=X)

        #        ==============first data frame================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE,
                          )
        Dataframe.place(x=0, y=130,
                        width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe,
                                   bd=10, relief=RIDGE,
                                   padx=20,
                                   font=('times new roman', 12, 'bold'),
                                   text='Patient Information')
        DataframeLeft.place(x=0, y=5, width=980,
                            height=350)

        DataframeRight = LabelFrame(Dataframe,
                                    bd=10, relief=RIDGE,
                                    padx=20,
                                    font=('times new roman', 12, 'bold'),
                                    text='Prescription')
        DataframeRight.place(x=990, y=5, width=460,
                             height=350)

        #         ===================buttons frame=============================

        Buttonframe = Frame(self.root, bd=20, relief=RIDGE,
                            )
        Buttonframe.place(x=0, y=530,
                          width=1530, height=70)

        #         ===================details frame=============================

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE,
                             )
        Detailsframe.place(x=0, y=600,
                           width=1530, height=190)

        #         =======================dataframe left ===================
        lblNameTablet = Label(DataframeLeft, text="Names of Tablet",
                              font=('times new roman', 12, 'bold'),
                              padx=2,
                              pady=6
                              )
        lblNameTablet.grid(row=0, column=0)

        comNametablet = ttk.Combobox(DataframeLeft,
                                     font=('times new roman', 12, 'bold'),
                                     width=33,
                                     textvariable=self.Nameoftablets
                                     )

        comNametablet['values'] = (
            'Nice',
            'Corona Vaccine',
            'Napa Extra',
            'Nightfresh',
            'Sinafresh',
            'Omiprajol'
        )

        comNametablet.current(0)

        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft,
                       font=('times new roman', 12, 'bold'),
                       text='Reference No',
                       padx=2
                       )

        lblref.grid(row=1, column=0, sticky=W)

        textref = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.ref,

            width=35
        )
        textref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft,
                        font=('times new roman', 12, 'bold'),
                        text='Dose',
                        padx=2
                        )

        lblDose.grid(row=2, column=0, sticky=W)

        textDose = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.Dose,

            width=35
        )
        textDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataframeLeft,
                               font=('times new roman', 12, 'bold'),
                               text='No Of Tablets',
                               padx=2
                               )

        lblNoOfTablets.grid(row=3, column=0, sticky=W)

        textNoOfTablets = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.NumberofTablets,

            width=35
        )
        textNoOfTablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft,
                       font=('times new roman', 12, 'bold'),
                       text='Lot:', padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)

        textLot = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.Lot,

            width=35
        )
        textLot.grid(row=4, column=1)

        lblissueDate = Label(DataframeLeft,
                             font=('times new roman', 12, 'bold'),
                             text='Issue Date:', padx=2, pady=6)
        lblissueDate.grid(row=5, column=0, sticky=W)

        textissueDate = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.Issuedate,

            width=35
        )
        textissueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft,
                           font=('times new roman', 12, 'bold'),
                           text='Exp Date:', padx=2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)

        textExpDate = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.ExpDate,

            width=35
        )
        textExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft,
                             font=('times new roman', 12, 'bold'),
                             text='Daily Dose:', padx=2, pady=6
                             )
        lblDailyDose.grid(row=7, column=0, sticky=W)

        textDailyDose = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            width=35,
            textvariable=self.DailyDose
        )
        textDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft,
                              font=('times new roman', 12, 'bold'),
                              text='Side Effect:', padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)

        textSideEffect = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            width=35,
            textvariable=self.sideEffect
        )
        textSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataframeLeft,
                               font=('times new roman', 12, 'bold'),
                               text='Further Information', padx=2, pady=6)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)

        textFurtherinfo = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            width=35,
            textvariable=self.FurtherInformation
        )
        textFurtherinfo.grid(row=0, column=3)

        lblDrivingMachine = Label(DataframeLeft,
                                  font=('times new roman', 12, 'bold'),
                                  text='Blood Pressure', padx=2, pady=6)
        lblDrivingMachine.grid(row=1, column=2, sticky=W)

        textDrivingMachine = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            textvariable=self.DrivingUsingMachine,

            width=35
        )
        textDrivingMachine.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft,
                           font=('times new roman', 12, 'bold'),
                           text='Storage Advice', padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)

        textStorage = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.StorageAdvice,

            width=35
        )
        textStorage.grid(row=2, column=3)

        lblMedicine = Label(DataframeLeft,
                            font=('times new roman', 12, 'bold'),
                            text='Medication', padx=2, pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)

        textMedicine = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),


            width=35
        )
        textMedicine.grid(row=3, column=3
                          , sticky=W)

        lblPatientId = Label(DataframeLeft,
                             font=('times new roman', 12, 'bold'),
                             text='Patient Id', padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)

        textPatientId = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),

            width=35
        )
        textPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft,
                             font=('times new roman', 12, 'bold'),
                             text='NHS Number', padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)

        textNhsNumber = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.nhsNumber
            ,

            width=35
        )
        textNhsNumber.grid(row=5, column=3)

        lblPatientname = Label(DataframeLeft,
                               font=('times new roman', 12, 'bold'),
                               text='Patient Name', padx=2, pady=6)
        lblPatientname.grid(row=6, column=2, sticky=W)

        textPatientname = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.PatinetName,

            width=35
        )
        textPatientname.grid(row=6, column=3)

        lblDateOfBirth = Label(DataframeLeft,
                               font=('times new roman', 12, 'bold'),
                               text='Date Of Birth', padx=2, pady=6)
        lblDateOfBirth.grid(row=7, column=2, sticky=W)

        textDateOfBirth = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.DateOfBirth,

            width=35
        )
        textDateOfBirth.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft,
                                  font=('times new roman', 12, 'bold'),
                                  text='Patient Address', padx=2, pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)

        textPatientAddress = Entry(
            DataframeLeft,
            font=('times new roman', 13, 'bold'),
            textvariable=self.PatientAddress,

            width=35
        )
        textPatientAddress.grid(row=8, column=3)

        #         =====================DATAFRAME RIGHT============================
        self.txtPrescription = Text(DataframeRight,
                                    font=('times new roman', 13, 'bold'),
                                    width=45,
                                    height=16,
                                    padx=2,
                                    pady=6
                                    )

        self.txtPrescription.grid(row=0, column=0)

        #          ==============================================buttons=====================
        btnPrescription = Button(Buttonframe,
                                 text='Prescription',
                                 bg='green',
                                 fg='white',
                                 font=('times new roman', 12, 'bold'),
                                 width=23,
                                 # height=10,
                                 padx=2,
                                 pady=6,
                                 command=self.iPrectioption

                                 )
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe,
                                     text='Prescription Data',
                                     bg='green',
                                     fg='white',
                                     font=('times new roman', 12, 'bold'),
                                     width=23,
                                     # height=10,
                                     padx=2,
                                     pady=6,
                                     command=self.iPrescriptionData

                                     )
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe,
                           text='Update',
                           bg='green',
                           fg='white',
                           font=('times new roman', 12, 'bold'),
                           width=23,
                           # height=10,
                           padx=2,
                           pady=6,

                           command=self.update_data

                           )
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe,
                           text='Delete',
                           bg='green',
                           fg='white',
                           font=('times new roman', 12, 'bold'),
                           width=23,
                           # height=10,
                           padx=2,
                           pady=6,

                           command=self.idelete

                           )
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe,
                          text='Clear',
                          command=self.clear,
                          bg='green',
                          fg='white',
                          font=('times new roman', 12, 'bold'),
                          width=23,
                          # height=10,
                          padx=2,
                          pady=6,

                          )
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe,
                         text='Exit',
                         bg='green',
                         fg='white',
                         font=('times new roman', 12, 'bold'),
                         width=23,
                         # height=10,
                         padx=2,
                         pady=6,
                         command=self.iExit

                         )
        btnExit.grid(row=0, column=5)

        #         ====================table ========================

        #         =================scrollbar ============================

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe,
                                           columns=(
                                               "nameoftable",
                                               "ref",
                                               "dose",
                                               "nooftablets",
                                               "lot",
                                               "issuedate",
                                               "expdate",
                                               "dailydose",
                                               "storage",
                                               "nhsnumber",
                                               "pname",
                                               "dob",
                                               "address"
                                           ),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable", text='Name of Table')
        self.hospital_table.heading("ref", text='Reference No.')
        self.hospital_table.heading("dose", text='Dose')
        self.hospital_table.heading("nooftablets", text='No of Tablets')
        self.hospital_table.heading("lot", text='Lot')
        self.hospital_table.heading("issuedate", text='Issue Date')
        self.hospital_table.heading("expdate", text='Exp Date')
        self.hospital_table.heading("dailydose", text='Daily Dose')
        self.hospital_table.heading("storage", text='Storage')
        self.hospital_table.heading("nhsnumber", text='NHS Number')
        self.hospital_table.heading("pname", text='Patient Name')
        self.hospital_table.heading('dob', text='DOB')
        self.hospital_table.heading('address', text='Address')

        self.hospital_table['show'] = 'headings'

        self.hospital_table.column("nameoftable", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)

        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_date()

    #         ============================functionality declaration==================

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == '' or self.ref.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            conn = mysql.connector.connect(
                host='localhost',
                username='root',
                password='1234',
                database='hospitalmanagement'
            )

            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.Nameoftablets.get(),
                self.ref.get(),
                self.Dose.get(),
                self.NumberofTablets.get(),
                self.Lot.get(),
                self.Issuedate.get(),
                self.ExpDate.get(),
                self.DailyDose.get(),
                self.StorageAdvice.get(),
                self.nhsNumber.get(),
                self.PatinetName.get(),
                self.DateOfBirth.get(),
                self.PatientAddress.get()))
            conn.commit()
            self.fetch_date()
            conn.close()

            messagebox.showinfo("Success", "Record has been inserted")



    def update_data(self):

        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hospitalmanagement'
        )

        my_cursor = conn.cursor()
        my_cursor.execute('update hospital set nameoftablets=%s,dose=%s,numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,dob=%s,patientaddress=%s where referenceno=%s',(
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatinetName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get()
        ))
        conn.commit()
        self.fetch_date()
        conn.close()

        messagebox.showinfo("Success", "Record has been updated")

    def fetch_date(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hospitalmanagement'
        )

        my_cursor = conn.cursor()
        my_cursor.execute('select * from hospital')
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cursor_row = self.hospital_table.focus()
        content =self.hospital_table.item(cursor_row)
        row = content['values']
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatinetName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])


    def iPrectioption(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.ExpDate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+self.PatinetName.get()+"\n")
        self.txtPrescription.insert(END,"DateofBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")




    def idelete(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='1234',
            database='hospitalmanagement'
        )

        my_cursor = conn.cursor()

        query = 'delete from hospital where referenceno=%s'
        value = (self.ref.get(),)

        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_date()

        messagebox.showinfo("Success", "Record has been deleted")

    def clear(self):
        self.Nameoftablets.set('')
        self.ref.set('')
        self.Dose.set('')
        self.NumberofTablets.set('')
        self.Lot.set('')
        self.Issuedate.set('')
        self.ExpDate.set('')
        self.DailyDose.set('')
        self.sideEffect.set('')
        self.FurtherInformation.set('')
        self.StorageAdvice.set('')
        self.DrivingUsingMachine.set('')
        self.HowToUseMedicine.set('')
        self.PatientId.set('')
        self.nhsNumber.set('')
        self.PatinetName.set('')
        self.DateOfBirth.set('')
        self.PatientAddress.set('')
        self.txtPrescription.delete('1.0',END)

    def iExit(self):
        iexit = messagebox.askyesno(
            'Hospital management system',
            'Confirm you want to exit'
        )

        if iexit>0:
            root.destroy()
            return












root = Tk()
obj = Hospital(root)
root.mainloop()
