/*
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

*/

class LRUCache{
	class Node{
		int key;
		int value;
		Node prev;
		Node next;
	}
	
	private void addNode(Node node){
		node.prev = head;
		node.next = head.next;
		head.next.prev = node;
		head.next = node;
	}
	
	private void removeNode(Node node){
		Node previous = node.prev;
		Node next = node.next;
		previous.next = next;
		next.prev = previous;
	}
	
	private void moveNodeToFront(Node node){
		this.removeNode(node);
		this.addNode(node);
	}
	
	private Node removeLastElement(){
		Node lastprev = tail.pre;
		this.removeNode(lastprev);
		return lastprev;
	}
	
	private HashMap<Integer,Node> hash = new HashMap<>();
	private int count;
	private int capacity;
	private Node head,tail;
	
	public LRUCache(int capacity){
		this.count = 0;
		this.capacity = capacity;
		head = new Node();
		head.prev = null;
		tail = new Node();
		tail.next = null;
		head.next = tail;
		tail.prev = head;
	}
	
	public int get(int key){
		Node node = hash.get(key);
		if(node == null){
			return -1;
		} 
		this.moveNodeToFront(node);
		return node.value;
	}
	
	public void put(int key,int value){
		Node node = hash.get(key);
		if(node == null){
			Node newnode = new Node();
			newnode.key = key;
			newnode.value = value;
			this.hash.put(key,newnode);
			this.addNode(newnode);
			++count;
			if(count>capacity){
				Node tail = this.removeLastElement();
				this.hash.remove(tail.key);
				--count;
			}
		}
		else{
			node.value = value;
			this.moveNodeToFront(node);
		}
	}
}
