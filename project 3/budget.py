class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
    def get_balance(self):
        return sum(l["amount"] for l in self.ledger)
    def withdraw(self, amount, description = ""):
        funds_are_enough = self.check_funds(amount)
        if(funds_are_enough):
            self.deposit(-1*amount, description)
        return funds_are_enough  
    def check_funds(self, amount):
        if(self.get_balance() < amount):
            return False
        return True
    def transfer(self, amount, transference_category):
        funds_are_enough = self.check_funds(amount)
        if(funds_are_enough):
            self.withdraw(amount, "Transfer to " + transference_category.name)
            transference_category.deposit(amount, "Transfer from " + self.name)
        return funds_are_enough
    def __str__(self):
        representation = ""
        header_asterisk_count = 30 - len(self.name)
        header = header_asterisk_count//2 * "*" + self.name + header_asterisk_count//2 * "*"

        representation += header + "\n"

        '''maximum_digits = max(len("{:.2f}".format(item["amount"])) for item in self.ledger)'''
      
        for item in self.ledger:
            cur_line = item["description"][:23]
            cur_line = cur_line.ljust(23)
            cur_line += "{:.2f}".format(item["amount"]).rjust(7)
            representation += cur_line + "\n"
        
        representation += "Total: " + "{:.2f}".format(self.get_balance())

        return representation
            


def create_spend_chart(categories):
    header = "Percentage spent by category"
    chart = header #+ "\n"
    spends = []
    for category in categories:
        spends.append(sum([item["amount"] * -1 for item in category.ledger if item["amount"] < 0]))
    total_spend = sum(spends)

    spend_percentages = [ int((spend * 100) // total_spend) for spend in spends]

    #print( spend_percentages )

    for i in range(100, -1, -10):
        chart += "\n" + str(i).rjust(3) + "|"
        for j in spend_percentages:
            if j >= i:
                chart += " o "
                continue
            chart += "   "
        chart += " "
    chart += "\n    ----------"

    cat_length = []
    for category in categories:
        cat_length.append(len(category.name))
    max_length = max(cat_length)

    for i in range(max_length):
        chart += "\n    "
        for j in range(len(categories)):
            if i < cat_length[j]:
                chart += " " + categories[j].name[i] + " "
                continue
            chart += "   "
        chart += " "
    return chart

    '''for percentage in range(100, -1, -10):
        chart += (str(percentage) + "|").rjust(4)
        
        for spend_percentage in spend_percentages:

            if spend_percentage > percentage or percentage < 10: 
                chart += " o "
            else:
                chart += "   "
        chart = chart.ljust(14)
        chart +=  "\n"
    
    chart += (" " * 4) + (((3 * len(categories)) + 1) * "-") + "\n"
    
    max_name_size = max([len(category.name) for category in categories])
    
    for i in range(max_name_size):
        chart += (" " * 4)
        for category in categories:
            temp_category = category.name.ljust(max_name_size)
            chart += " " + temp_category[i] + " "
        chart += "\n"

    print(chart)
    return chart'''