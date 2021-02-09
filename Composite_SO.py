def main():
    file = open(r"\NYSE_Penny_Stocks_$10.txt",'r')
    file1 = open(r"\NASDAQ_Penny_Stocks_$10.txt",'r') 
    file2 = open(r"Merged.txt", 'w')
    NYSE_list = []
    NASDAQ_list = []
    COMP_list = []
       
    
    for line in file:
                
        this_line = line
        
        ticker = this_line.rsplit('\t',1)[0]
        
        #gets a list of stock tickers
        NYSE_list.append(this_line)    
    
    
    for line in NYSE_list:
        
        #lazy way of fixing text file problems
        
        ticker = line.rsplit('\t',1)[0]     
        
        tickers = ticker.rsplit(',')
        
        tickers[0]= tickers[0][1:]
        
        tickers[1] = tickers[1][:-1]
        
        price = tickers[1]
        
        price = price.strip()
        
        price = price[1:-1]
        
        price = price[:-1]
        
        ticker = tickers[0]
        
        ticker = ticker[1:-1]
        
        COMP_list.append((ticker,price))
        
        #print(ticker,price)
        
    
    
    for line in file1:
                
        this_line = line
        
        ticker = this_line.rsplit('\t',1)[0]
        
        #gets a list of stock tickers
        NASDAQ_list.append(this_line)    
    
    
    for line in NASDAQ_list:
        
        #lazy way of fixing text file problems
        
        ticker = line.rsplit('\t',1)[0]     
        
        tickers = ticker.rsplit(',')
        
        tickers[0]= tickers[0][1:]
        
        tickers[1] = tickers[1][:-1]
        
        price = tickers[1]
        
        price = price.strip()
        
        price = price[1:-1]
        
        price = price[:-1]
        
        ticker = tickers[0]
        
        ticker = ticker[1:-1]
        
        if ticker not in COMP_list:
        
            COMP_list.append((ticker,price))
       
    COMP_list.sort(key = lambda x: x[0])
    #print(COMP_list)
    
    for line in COMP_list:
        
        this_line ="('" + line[0]+', ' + line[1] + "')" '\n'
        
        file2.write(this_line)




    file.close()
    file1.close()
    file2.close()    
main()
