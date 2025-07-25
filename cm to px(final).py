from pyscript import display
from js import document
import js

def enter(event=None):
    form_choice = document.querySelector('input[name="type"]:checked').value
    dpi = float(document.querySelector('select').value)
    num_value = document.getElementById("num").value

    if num_value == "":
        js.alert("Please enter a number before clicking Enter!")
        return
    num = float(num_value)

    if num < 0:
        js.alert("This number is negative!")
        return
    elif num > 1000000.0:
        js.alert("Please enter a number that is less than 1.000.000.0!")
        return

    if form_choice=='1':
        r=(num/2.54)*dpi
        r=round(r,2)
        document.getElementById("result").innerText = f"The {num} cm to px is: {r}"
    elif form_choice=='2':
        r=(num/dpi)*2.54
        r=round(r,2)
        document.getElementById("result").innerText = f"The {num} px to cm is: {r}"
def clear(event=None):
    document.getElementById("myinput1").checked = True
    document.getElementById("DPI").value="96"
    document.getElementById("num").value=""
    document.getElementById("result").innerText =""
    
