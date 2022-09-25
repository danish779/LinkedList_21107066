class Node:
    def __init__(self,name,age):
        self.name = name; 
        self.age=age; 
        self.previous = None;  
        self.next = None;   
          
class DoublyLinkedList:
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
           
    def addNode(self, name,age):  
        newNode = Node(name,age);  
           
        if(self.head == None):   
            self.head = self.tail = newNode;  
            self.head.previous = None; 
            self.tail.next = None;  
        else:  
            self.tail.next = newNode;  
            newNode.previous = self.tail; 
            self.tail = newNode; 
            self.tail.next = None;  
   

    def display(self):
         value_list=[]
         if(self.head != None): 
            current_node = self.head 
            while current_node.next != None: 
                value_list.append([current_node.name,current_node.age])
                current_node = current_node.next 
            value_list.append([current_node.name,current_node.age])
            print("Doubly linked list of family: "); 
            print(value_list)
         else: 
            print("No node")
            return False
              
dList = DoublyLinkedList(); 
dList.addNode("Junaid Akhtar",47);  
dList.addNode("Husn Ara Khatoon",43);  
dList.addNode("Danish Akhtar",19); 
dList.display();


#OUTPUT:
#Doubly linked list of family: 
#[['Junaid Akhtar', 47], ['Husn Ara Khatoon', 43], ['Danish Akhtar', 19]]


    

