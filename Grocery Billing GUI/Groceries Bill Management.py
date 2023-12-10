#!/usr/bin/env python
# coding: utf-8

# In[9]:


from tkinter import *
bill={}
def save_bill_click(self):
    print('Bill saved')
    print(bill)
def add_to_bill_click(self):
    indexes=[]
    qty=(e3.get())
    indexes=lb1.curselection()
    for i in indexes:
        list_for_qty_remain[i]-=int(qty)
        bill.update({list_for_lb1[i] : int(qty)*list_for_cost[i]})
    for i in range(0,6):
        lb2.delete(ACTIVE,i)
def refresh_stock_click(self):
     for i in list_for_qty_remain:
        lb2.insert(ANCHOR,i)
def printing_bill_click(self):
    print(f'Customer Name :  {e1.get()}')
    print('Item                                  Cost(In Rs)')
    total=0
    for i in bill:
        total+=bill[i]
    bill.update({'Total' : total})
    for i,j in bill.items():
        print(f'{i}                                      {j}')
def reset_bill_click(self):
    bill.clear()
    for i in range(0,6):
        lb2.delete(ACTIVE,i)
root=Tk()
root.geometry('1000x500')
root.title('Billing')
f=Frame(root,height=450,width=1000)
f.propagate(0)
f.pack()
m1=Message(f,width=1000,text='---------------------------------------------------------------------------------Billing-----------------------------------------------------------------------')
#m1.pack(side=TOP,fill=X)
m1.place(y=10)
l1=Label(text='Enter Name:  ')
l2=Label(text='Enter Address:')
e1=Entry(f)
e2=Entry(f)
l1.place(x=50,y=50)
l2.place(x=50,y=75)
e1.place(x=200,y=50)
e2.place(x=200,y=75)
b1=Button(f,text='Main Menu',width=20)
b1.place(x=850,y=40)
b2=Button(f,text='Refresh Stock',width=20)
b2.bind('<Button-1>',refresh_stock_click)
b2.place(x=850,y=90)
b3=Button(f,text='Reset Bill',width=20)
b3.bind('<Button-1>',reset_bill_click)
b3.place(x=850,y=115)
b4=Button(f,text='Print Bill',width=20)
b4.bind('<Button-1>',printing_bill_click)
b4.place(x=850,y=140)
m2=Message(width=1000,text='---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
m2.place(y=170)
select_item=Button(f,text='Select Item',width=20)
select_item.place(x=50,y=200)
lb1=Listbox(f,width=30,selectmode=SINGLE)
lb1.place(x=30,y=230)
list_for_lb1=['Milk','Sandwich Wheat','Chai','Chocolate','Cake','Marie']
for i in list_for_lb1:
    lb1.insert(END,i)
qty_remain=Button(f,text='Qty_remain',width=20)
qty_remain.place(x=250,y=200)
lb2=Listbox(f,width=15,bg='white')
lb2.place(x=260,y=230)
list_for_qty_remain=lqr=[100,93,98,343,113,122]
cost=Button(f,text='Cost',width=7)
cost.place(x=440,y=200)
lb3=Text(f,width=9)
lb3.place(x=435,y=230)
list_for_cost=[10.99,9.99,6.99,1.33,12.99,2.99]
for i in list_for_cost:
    lb3.insert(END,i)
    lb3.insert(END,'\n')
expiry_date=Button(f,text='Expiry Date',width=15)
expiry_date.place(x=540,y=200)
lb4=Text(f,width=20)
lb4.place(x=520,y=230)
list_for_expiry_date=['12/12/2017','08/31/2017','12/05/2018','12/12/2016','12/12/2018','12/02/2016']
for i in list_for_expiry_date:
    lb4.insert(END,i)
    lb4.insert(END,'\n')
quantity=Button(f,text='Quantity',width=15)
quantity.place(x=700,y=200)
e3=Entry(f,width=15)
e3.place(x=700,y=320)
save_bill=Button(f,width=20,text='Save Bill')
save_bill.bind('<Button-1>',save_bill_click)
save_bill.place(x=830,y=200)
add_to_bill=Button(f,width=20,text='Add to bill')
add_to_bill.bind('<Button-1>',add_to_bill_click)
add_to_bill.place(x=830,y=350)
for i in list_for_qty_remain:
        lb2.insert(END,i)
root.mainloop()


# In[ ]:




