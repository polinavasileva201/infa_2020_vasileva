#include <iostream>
#include <stack>
using namespace std;

struct subset_node {
    int key;
    subset_node *left;
    subset_node *right;
};

//иницилизация пустого дерева
bool init(subset_node **sn) {
    *sn = NULL;
    return true;
};

//добавление элемента в дерево
bool insert(subset_node **sn, int k) {
    if (*sn == NULL) {
        subset_node *cur = new subset_node;
        cur->key = k;
        cur->left = NULL;
        cur->right = NULL;
        *sn = cur;
        return true;
    }
    if (k == (**sn).key) return false;
    
    if (k > (**sn).key) insert(&(**sn).right, k);
    
    if (k < (**sn).key) insert(&(**sn).left, k);
    
};


//удаление элемента из дерева
bool remove(subset_node **sn, int k) {
    if (*sn ==NULL) return false;
    
    if (k == (**sn).key) return (*sn);
    
    if (k > (**sn).key) {
        subset_node *right = (**sn).right;
        if (k == (*right).key) (**sn).right = (*right).left;
        
    }
    if (k < (**sn).key) {
        subset_node *left = (**sn).left;
        if (k == (*left).key) (**sn).left = (*left).left;
        
    }
};



//поиск элемента в дереве
subset_node* find(subset_node **sn, int k) {
	if (*sn==NULL) return NULL;  
	   
	if (k == (**sn).key) return (*sn); 
	   
	if (k <= (**sn).key){
	  if ((**sn).left != NULL) return find(&(**sn).left, k); 
	  else return NULL;      
	}
	else {
	  if ((**sn).right) return find(&(**sn).right, k);
	  else return NULL; 
    }
};



//количество элементов в дереве
unsigned int size(subset_node **sn) {
   unsigned int size = 0;
   stack <subset_node*> st;
  do
  {
    while ((*sn) != 0)
    {
      st.push(*sn);
      (*sn) = (*sn)->left;
    }
    if (st.empty()) return size-1;
    (*sn) = st.top();
    st.pop();
    if ((**sn).right == NULL)++size;
    if ((**sn).left == NULL) ++size;
    (*sn) = (*sn)->right;
  }
  while (true);

};

//высота дерева
unsigned int height(subset_node **sn) {
    int left, right, h = 0;
    if((*sn) != NULL){
        left = height(&(**sn).left);
        right = height(&(**sn).right);
        h = ((left > right) ? left : right) + 1;
    }
    return h;
};

//очитстить всю используемую память
void destructor(subset_node **sn) {
	if ((**sn).left)   destructor(&(**sn).left); 
    if ((**sn).right)  destructor(&(**sn).right); 
    delete *sn;
};

//обход в глубину, возвращает указатль на массив
int* DFS(subset_node **sn) {
};


	
