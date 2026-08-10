# **Annex B**
## **Computational Thinking Exercise: "Smart Vending Machine"**
Section: 9 - Samat ------------------------- Score:____________

C# / Name:  #13 - Xian Gabriel D. Panganiban  Date: 10/08/2026

### **Scenario**

Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues:

- Sometimes the machine does not give the correct change.
- Items run out, but the machine doesn’t notify anyone.
- Students press the wrong buttons and get the wrong item.
- The machine is slow when multiple students use it in succession.

Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

### **Step 1: Identify the Big Problem**

Main Problem:

The machine is unreliable with the occasional financial and counting errors, and inefficient too because it has no safeguards against accidental uses and heavy student traffic.

### **Step 2: Identify three to four Sub-Problems**

Please list possible sub-problems:

1. Incorrect calculations give the wrong amount of change the buyers receive.
2. The available stock is not shown real-time, which prevents the buyers and operators from knowing if the machine has been restocked.
3. The lack of a confirmation process before a buyer receives their item leads to accidental purchases.
4. The process takes too long to process payments and dispense items, therefore forming long lines.

### **Step 3: Define Computational Thinking Approaches**

For each sub-problem, apply CT skills:

| Sub-Problem | CT Skill | Example Solution |
|:--------|:------:|:----------|
| Long Processing Time | Decomposition | Decompose the steps of processing, like payments, exchange, and item dispensing, into individual steps for easier and faster management.|
| Lack of Alert When Stock Is Empty | Pattern Recognition | Use trends like times in the day the machine is most used to know when is the best time to stock up the machine while using notifiers like small lights to alert when the stock is low. |
| Button Accidents | Abstraction | Ignore physical design or size of the buttons, just focus on a confirmation for the order selected to avoid any mistakes by students. |
| Incorrect Calculations | Algorithm Designs | Separate each step of calculating change, such as counting the received money, subtracting the total price from it, and returning the change. |

### **Step 4: Draw a flowchart or write a pseudocode for the identified subproblem**

For Sub-problem 2:
```
START

#For the vending machine staff:
INPUT every item_name and item_price in the vending machine list
INPUT initial item_stock

#For the customer:
INPUT every item_to_dispense
INPUT every item_amount
INPUT buy_confirm
INPUT payment

#Machine algorithm
SET total_cost = 0
SET stock_available = TRUE

FOR every unique item_to_dispense DO:
    IF item_stock < all of this item_amount THEN:
        SET stock_available = FALSE
    SET total_cost = total_cost + (item_price * item_amount)

IF buy_confirm is TRUE and stock_available is TRUE and payment >= total_cost THEN:
    FOR every item_to_dispense DO:
        DISPLAY item_amount + " of " + item_to_dispense + " bought!"
        DO item_stock = item_stock - item_amount
        DISPENSE item_amount of item_to_dispense

    DISPENSE payment - total_cost

ELSE:
    DISPLAY "Transaction failed."
    IF stock_available is FALSE THEN:
        DISPLAY "Stock too low and needs restocking."
    DISPENSE payment

FOR every item_name DO:
    IF item_stock = 0 THEN:
        DISPLAY "Alert! item is out of stock. Please restock."

END
```
