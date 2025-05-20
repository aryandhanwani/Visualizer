import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:

    class sales_data_analyzer:
    
        def __init__(self):
            self.data_loaded = False
        
        def load_data(self):
            if self.data_loaded==False:
                self.data_loaded=True
                self.__df__=pd.read_csv("sales_data_analyzer_sample.csv")
                print(self.__df__.head(),"\n")
                print("Data Loaded Success Fully\n")
            
            else:
                print("Data is already Loaded\n")
        
        def explore_data(self):
            
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
             
            else:
                while True:
                    print("1. Display the First 5 Rows")
                    print("2. Display the Last 5 Rows")
                    print("3. Display Data Types")
                    print("4. Display the Size of Data")
                    print("5. Display the Basic information")
                    print("6. Back to main menu")
    
                    choice2=int(input("Enter your choice: "))
                    print() 
    
                    if choice2==1:
                        print(self.__df__.head(),"\n")
    
                    elif choice2==2:
                        print(self.__df__.tail(),"\n")
    
                    elif choice2==3:
                        print(self.__df__.dtypes,"\n")
    
                    elif choice2==4:
                        print(self.__df__.size,"\n")
    
                    elif choice2==5:
                        print(self.__df__.info(),"\n")
    
                    elif choice2==6:
                        break
                    
                    else:
                        print("Invalid Choice\n")
    
        def mathematical_operations(self):
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
           
            else:
                self.__col__=input(f"Enter the numeric column name from {self.__df__.columns}")
                print()
    
                if self.__col__ in self.__df__.columns:
                    print(f"Sum Value of {self.__col__} is {self.__df__[self.__col__].sum()}\n")
                    print(f"Average Value of {self.__col__} is {self.__df__[self.__col__].mean()}\n")
                    print(f"Miniman Value of {self.__col__} is {self.__df__[self.__col__].min()}\n")
                    print(f"Maximum Value of {self.__col__} is {self.__df__[self.__col__].max()}\n")
                
                else:
                    print("The Entered column is invalid\n")
        
        def combine_data(self):
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
            
            else:
                filepath=input("Enter the File Path: ")
                print()
                self.__new_df__=pd.read_csv(filepath)
                self.__df__=pd.concat([self.__df__,self.__new_df__],ignore_index=True)
                print(self.__df__.head())
                print("\n Data Frame Combined\n")
        
        def search_sort_filter(self):
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
            
            else:
                print("1. Search Data")
                print("2. Sort Data")
                print("3. Filter Data")
    
                choice4=int(input("Enter your choice: "))
                print()
    
                if choice4==1:
                    self.__col__=input(f"Enter the column name from {self.__df__.columns}: ")
                    print()
    
                    if self.__col__ in self.__df__.columns:
                        self.__value__=input("Enter the Value to search: ")
    
                        print(self.__df__[self.__df__[self.__col__]==self.__value__])
    
                    else:
                        print("Entered Column is invalid\n") 
    
                elif choice4==2:
                    self.__col__=input(f"Enter the column name from {self.__df__.columns}: ")
                    print()
    
                    if self.__col__ in self.__df__:
                        print("1. For Ascending Order Sorting")
                        print("2. For Descending Order Sorting")
    
                        choice5=int(input("Enter your choice: "))
                        print()
    
                        if choice5==1:
                            print(self.__df__.sort_values(by=self.__col__, ascending=True),"\n")
    
                        elif choice5==2:
                            print(self.__df__.sort_values(by=self.__col__, ascending=False),"\n")
    
                        else:
                            print("Invalid Choice\n")
    
                elif choice4==3:
                    self.__col__=input(f"Enter the column name from {self.__df__.columns}: ")
                    print()
    
                    if self.__col__ in self.__df__.columns:
                        self.__value__=input("Enter the Value to Filter: ")
    
                        print(self.__df__[self.__df__[self.__col__]==self.__value__])
                    else:
                        print("Entered Column is invalid\n") 
    
                else:
                    print("Invalid Choice\n")
    
        def aggregation_functions(self):
            
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
            
            else:
                self.__col__=input(f"Enter the column name from {self.__df__.columns}: ")
                print()
    
                if self.__col__ in self.__df__.columns:
                    print(f"Sum of {self.__col__} is {self.__df__[self.__col__].sum()}\n")
                    print(f"Average of {self.__col__} is {self.__df__[self.__col__].mean()}\n")
                    print(f"Minimum of {self.__col__} is {self.__df__[self.__col__].min()}\n")
                    print(f"Maximum of {self.__col__} is {self.__df__[self.__col__].max()}\n")
                    print(f"Standard Daviation of {self.__col__} is {self.__df__[self.__col__].std()}\n")
                    print(f"Variance of {self.__col__} is {self.__df__[self.__col__].var()}\n")
                
                else:
                    print("Entered Column is invalid\n")
    
        def statistical_analysis(self):
        
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
            
            else:
                self.__col__=input(f"Enter the column name from {self.__df__.columns}: ")
                print()
    
                if self.__col__ in self.__df__:
                    print(f"Statistical analysis of {self.__col__} is:\n{self.__df__[self.__col__].describe()}\n")
                
                else:
                    print("Entered Column is invalid\n")
                    print("Entered Column is invalid\n")
    
        def pivottable(self):
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
            
            else:
                ind=input(f"Enter the Column Name for Index from {self.__df__.columns}: ")
                col=input(f"Enter the Column Name for Columns from {self.__df__.columns}: ")
                val=input(f"Enter the Column Name for Values from {self.__df__.columns}: ")
                ag=input(f"Enter the Aggregation function name form [mean, sum, min, max, std, var]: ").lower()
                print()
    
                if ind in self.__df__.columns and col in self.__df__.columns and val in self.__df__.columns:
                    print(pd.pivot_table(data=self.__df__, index=ind, columns=col, values=val, aggfunc=ag),"\n")
                
                else:
                    print("One of the Entered Column is invalid\n")
    
        def clean_data(self):
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
            
            else:
                print("1. Display Null Values")
                print("2. Fill Null with custom Values")
                print("3. Fill Null with Aggregation Functions")
                print("4. Drop the Null Values")
                print("5. Check Duplicated Values")
                print("6. Drop Duplicated")
    
                choice6=int(input("Enter the Choice: "))
                print()
    
                if choice6==1:
                    print(self.__df__.isna(),"\n")
                
                elif choice6==2:
                    val=input("Enter the Value: ")
                    print(self.__df__.fillna(val, inplace=True),"\n")
    
                elif choice6==3:
                    ag=input(f"Enter the Aggregation function name form [mean, sum, min, max, std, var]: ").lower()
                    print(self.__df__.fillna(self.__df__.agg(ag), inplace=True),"\n")
                
                elif choice6==4:
                    print(self.__df__.dropna())
                
                elif choice6==5:
                    print(self.__df__.duplicated())
                
                elif choice6==6:
                    print(self.__df__.drop_duplicates())
                else:
                    print("Invalid Choice\n")
    
        def visualization(self):
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
            else:
                print("1. Bar Plot")
                print("2. Line Plot")
                print("3. Scatter Plot")
                print("4. Pie Chart")
                print("5. Histogram")
                print("6. Stack Plot")
                print("7. Heatmap")
                print("8. Box Plot")
    
                choice7=int(input("Enter your choice: "))
                print()
    
                if choice7==1:
                    y=input(f"Enter the columns from {self.__df__.columns} for y-axis: ")
                    x=input(f"Enter the columns from {self.__df__.columns} for x-axis: ")
                    tit=input("Enter Graph title: ")
    
                    if x in self.__df__.columns and y in self.__df__.columns:
                        self.figure=plt.figure(figsize=(8,10))
                        plt.bar(self.__df__[x], self.__df__[y])
                        plt.xlabel(x)
                        plt.ylabel(y)
                        plt.title(tit)
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("One of the Entered Column is invalid\n")
    
                elif choice7==2:
                    x=input(f"Enter the columns from {self.__df__.columns} for x-axis: ")
                    y=input(f"Enter the columns from {self.__df__.columns} for y-axis: ")
                    tit=input("Enter Graph title: ")
    
                    if x in self.__df__.columns and y in self.__df__.columns:
                        self.figure=plt.figure(figsize=(8,10))
                        plt.plot(self.__df__[x], self.__df__[y])
                        plt.xlabel(x)
                        plt.ylabel(y)
                        plt.title(tit)
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("One of the Entered Column is invalid\n")
    
                elif choice7==3:
                    y=input(f"Enter the columns from {self.__df__.columns} for y-axis: ")
                    x=input(f"Enter the columns from {self.__df__.columns} for x-axis: ")
                    tit=input("Enter Graph title: ")
    
                    if x in self.__df__.columns and y in self.__df__.columns:
                        self.figure=plt.figure(figsize=(8,10))
                        plt.scatter(self.__df__[x], self.__df__[y])
                        plt.xlabel(x)
                        plt.ylabel(y)
                        plt.title(tit)
                        plt.xticks(rotation=45)
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("One of the Entered Column is invalid\n")
    
                elif choice7==4:
                    y=input(f"Enter the columns from {self.__df__.columns}: ")
                    operation=input(f"Enter the columns from {self.__df__.columns} for Operation: ")
                    tit=input("Enter Graph title: ")
    
                    if operation in self.__df__.columns and y in self.__df__.columns:
                        data = self.__df__.groupby(y)[operation].sum()
                        self.figure=plt.figure(figsize=(8,10))
                        plt.pie(data, autopct='%1.0f%%', labels=data.index)
                        plt.title(tit)
                        plt.legend(loc="best")
                        plt.show()
                    else:
                        print("One of the Entered Column is invalid\n")
    
                elif choice7==5:
                    y=input(f"Enter the columns from {self.__df__.columns} ")
                    bin_size=int(input("Enter the bin size in numbers: "))
                    tit=input("Enter Graph title: ")
                    xl=input("Enter the xlabel: ")
                    yl=input("Enter the ylabel: ")
    
                    if y in self.__df__.columns:
                        self.figure=plt.figure(figsize=(8,10))
                        plt.hist(self.__df__[y], bins=bin_size)
                        plt.xlabel(xl)
                        plt.ylabel(yl)
                        plt.title(tit)
                        plt.show()
                    else:
                        print("Invalid column\n")
    
                elif choice7==6:
                    y1=input(f"Enter the columns from {self.__df__.columns} for  bar 1 y-axis: ")
                    y2=input(f"Enter the columns from {self.__df__.columns} for  bar 2 y-axis: ")
                    y3=input(f"Enter the columns from {self.__df__.columns} for  bar 3 y-axis: ")
                    x=input(f"Enter the columns from {self.__df__.columns} for x-axis: ")
                    xl=input("Enter the xlabel: ")
                    yl=input("Enter the ylabel: ")
                    tit=input("Enter Graph title: ")
    
                    if x in self.__df__.columns and y1 in self.__df__.columns and y2 in self.__df__.columns and y3 in self.__df__.columns:
                        self.figure=plt.figure(figsize=(8,10))
                        x_vals = self.__df__[x]
                        y1_vals = self.__df__[y1]
                        y2_vals = self.__df__[y2]
                        y3_vals = self.__df__[y3]
    
                        plt.bar(x_vals, y1_vals, label=y1)
                        plt.bar(x_vals, y2_vals, bottom=y1_vals, label=y2)
                        bottom_c = y1_vals.values + y2_vals.values
                        plt.bar(x_vals, y3_vals, bottom=bottom_c, label=y3)
    
                        plt.xlabel(xl)
                        plt.ylabel(yl)
                        plt.title(tit)
                        plt.xticks(rotation=45)
                        plt.legend(loc="best")
                        plt.tight_layout()
                        plt.show()
                    else:
                        print("One of the Entered Column is invalid\n")
    
    
                elif choice7==7:
                    x=input(f"Enter the columns from {self.__df__.columns} for x axis: ")
                    y=input(f"Enter the columns from {self.__df__.columns}for y axis: ")
                    tit=input("Enter Graph title: ")
    
                    if x in self.__df__.columns and y in self.__df__.columns:
                        self.figure=plt.figure(figsize=(8, 10))
                        heat=self.__df__[[x, y]].corr()
                        sns.heatmap(heat, annot=True)
                        plt.title(tit)
                        plt.show()
                    else:
                        print("Invalid columns\n")
    
                elif choice7==8:
                    x = input(f"Enter the columns from {self.__df__.columns} for x axis: ")
                    y = input(f"Enter the columns from {self.__df__.columns} for y axis: ")
                    pal = input("Enter seaborn palette name (e.g., 'pastel', 'deep'): ")
                    tit = input("Enter Graph title: ")
    
                    if x in self.__df__.columns and y in self.__df__.columns:
                        self.figure=plt.figure(figsize=(8, 10))
                        sns.boxplot(x=x, y=y, data=self.__df__, palette=pal)
                        plt.title(tit)
                        plt.show()
                    else:
                        print("Invalid columns\n")
    
                else:
                    print("Invalid choice\n")
    
        def save_visualization(self):
            if self.data_loaded==False:
                print("Data is not Loaded yet. Please load the data first\n")
            else:
                filename = input("Enter file name to save the graph: ")
                self.figure.savefig(filename)
                
    
    sale=sales_data_analyzer()
    
    while True:
        print("========== Data Analysis & Visualization Program ==========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform Dataframe Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
    
        choice1=int(input("Enter your choice: "))
        print()
    
        if choice1==1:
            sale.load_data()
        
        elif choice1==2:
            sale.explore_data()
        
        elif choice1==3:
            while True:
                print("1. Mathematical Operations")
                print("2. Combine Data")
                print("3. Search Sort Filter")
                print("4. aggregation Functions")
                print("5. Statistical Analysis")
                print("6. Create Pivot Table")
                print("7. Back to main menu")
    
                choice3=int(input("Enter your choice: "))
                print()
    
                if choice3==1:
                    sale.mathematical_operations()
                
                elif choice3==2:
                    sale.combine_data()
                
                elif choice3==3:
                    sale.search_sort_filter()
                
                elif choice3==4:
                    sale.aggregation_functions()
                
                elif choice3==5:
                    sale.statistical_analysis()                        
                
                elif choice3==6:
                    sale.pivottable()
                
                elif choice3==7:
                    break
                
                else:
                    print("Invalid Choice\n")                                    
        
        elif choice1==4:
            sale.clean_data()
        
        elif choice1==5:
            sale.statistical_analysis()
        
        elif choice1==6:
            sale.visualization()
        
        elif choice1==7:
            sale.save_visualization()
        
        elif choice1==8:
            print("Exiting the Program....\n")
            break
        
        else:
            print("Invalid Choice....\n")

except Exception as e:
    print(f"An error occurred: {e}")
