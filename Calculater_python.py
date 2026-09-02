import tkinter as tk
from tkinter import ttk

window  = tk.Tk()

window.title("Fee Calculater")
window.geometry("400x300")

gender_var = tk.StringVar(value ="None")
category_var =tk.StringVar(value ="None")

def btn_click():
    gender =gender_var.get()
    category = category_var.get()


    if gender =="None" or category =="None":
        lbl_result.config(text ="Please select both gender and category!",forground = "red")
        return


    fee = 0
    if category =="General" and gender == "Male":
        fee = 1000

    elif category =="General" and gender == "Female":
      fee = 600

    elif category =="OBC" and gender == "Male": 
     fee = 800

    elif category =="OBC" and gender == "Female":
        fee = 500

    elif category =="SC" and gender == "Male":
       fee = 500
     
    elif category =="Sc" and gender == "Female":
       fee = 100


       lbl_result.config(text = f"Total Fee: {fee}" , forground ="black")


       lblfram_gender = ttk.LalelFram(window, text = "Select your gender:")
       lblframe_gender.pack(padx = 10,pady = 10, fill = "both", exand ="yes")

       rblmale = ttk.Radiobutton(lblframe_gender , text ="Male", value ="Male", veriable = gender_var)
       rblmale.pack(anchor ="w", padx =10, pady =2)
       rbfeamle = ttk.Radiobutton(lblframe_gender, text ="Female" , value ="Feamle", variable = gender_var)
       rbfeamle.pack(anchor = "w", padx = 10, pady = 2) 

       lblframe_category = ttk.LabelFrame(window,text ="Select your category:")
       lblframe_category.pack(padx = 10, pady = 10 ,fill ="both",expand ="yes")



       rblgeneral = ttk.Radiobutton(lblframe_category, text ="General", value ="General", variable = category_var)   
       rblgeneral.pack(anchor = "w", padx = 10 , pady = 2)     
       rblobc = ttk.Radiobutton(lblframe_category ,text ="OBC",value = "OBC",variable = category_var)
       rblobc.pack(anchor = "w", padx =10 , pady = 2)
       rbsc = ttk.Radiobutton(lblframe_category , text ="SC", value = "SC", variable = category_var)
       rbsc.pack(anchor ="w", padx = 10, pady =2)

       btnsubmit = ttk.Button(window, text ="Calculater Fee ", command = btn_click)
       btnsubmit.pack(pack = 10)

       lbl_result =ttk.Label(window ,text ="",font =("Arial",12, "bold"))
       lbl_result.pack(pady = 10 )



       window.mainloop()

