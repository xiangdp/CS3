# **Annex B**
## **Computational Thinking Exercise: "Smart Vending Machine"**
Section: __________________________________ Score:____________

C# / Name:_________________________________ Date: _____________

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

```
START
#For the vending machine staff:
INPUT every item_name and item_price in the vending machine list
INPUT the initial item_stock


#For the customer:
INPUT every item_to_dispense
INPUT every item_amount
INPUT buy_confirm
INPUT payment


#Machine algorithm
IF buy_confirm is TRUE and payment >= item_price of all item_to_dispense THEN:
    FOR every item_to_dispense, DO:
        IF item_stock > or = to item_amount THEN:
            DISPLAY “item_bought of item_to_dispense bought!”
            DO item_stock = item_stock - item_amount
            DISPENSE item_amount of item_to_dispense
            DISPENSE payment - item_price of all item to dispense
        ELSE:
            DISPLAY “Stock too low and needs restocking.”


        FOR every item_name, DO:
            IF item_stock = 0 THEN:
                DISPLAY “Alert! Item is out of stok. Please restock.”

ELSE:
    DISPLAY “Transaction failed.”

END
```


