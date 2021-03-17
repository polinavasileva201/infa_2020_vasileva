#include <iostream>
#include <vector>
using namespace std;

struct subvector {
    int *mas;
    unsigned int top;
    unsigned int capacity;
};

/*
//иницилизация пустого недовектора
bool init(subvector *qv) {
	vector<subvector> qv;
    return true;
};


//добавление элемента в конец недовектора
//с выделением дополнительной памяти при необходимости
bool push_back((subvector *qv, int d) {
	
	if (top > 0){
		if (top == capacity){
	            capacity *= 2;
	            int *tmp = new int[capacity];
	            memmove(tmp, mas, top * sizeof(int));
	            delete[] mas;
	            mas = tmp;
	        }
	        mas[top++] = d;
	}
};
*/

//удаление элемента с конца недовектора
int pop_back(subvector *qv) {
	if (top > 0){
            while (top < capacity){
                capacity--;}
            if (top == capacity){
                top--;
                capacity--;
                int* tmp = new int[top];
                memmove(tmp, mas, top * sizeof(int));
                delete[] mas;
                mas = tmp;}
        }
   
};


/*
//увеличить емкость недовектора
bool resize(subvector *qv, unsigned int new_capacity) {
	int newSize = qv.size();
	int new_capacity = qv.getCapacity();
	data = new T[new_capacity];
	for(int i = 0; i < newSize; i++)
	data[i] = qv.data[i];
	return *this;

		
};
*/


//очистить используемую память
void shrink_to_fit(subvector *qv) {
   
};

//очистить содержимое вектора, занимаемое место
//при этом не меняется
void clear(subvector *qv) {
};

//очитстить всю используемую память, инициализировать
//недовекор как пустой
void destructor(subvector *qv) {
};

//инициализировать недовектор из папки
bool init_from_file(subvector *qv, char *filename) {
};


	
