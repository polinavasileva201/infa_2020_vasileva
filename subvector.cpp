#include <iostream>
#include <vector>
using namespace std;

struct subvector {
    int *mas;
    unsigned int top;
    unsigned int capacity;
};

/*
//������������ ������� �����������
bool init(subvector *qv) {
	vector<subvector> qv;
    return true;
};


//���������� �������� � ����� �����������
//� ���������� �������������� ������ ��� �������������
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

//�������� �������� � ����� �����������
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
//��������� ������� �����������
bool resize(subvector *qv, unsigned int new_capacity) {
	int newSize = qv.size();
	int new_capacity = qv.getCapacity();
	data = new T[new_capacity];
	for(int i = 0; i < newSize; i++)
	data[i] = qv.data[i];
	return *this;

		
};
*/


//�������� ������������ ������
void shrink_to_fit(subvector *qv) {
   
};

//�������� ���������� �������, ���������� �����
//��� ���� �� ��������
void clear(subvector *qv) {
};

//��������� ��� ������������ ������, ����������������
//��������� ��� ������
void destructor(subvector *qv) {
};

//���������������� ���������� �� �����
bool init_from_file(subvector *qv, char *filename) {
};


	
