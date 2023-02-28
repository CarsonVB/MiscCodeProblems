#include<stdlib.h>
#include<vector>
#include<random>
#include <chrono>
#include <iostream>
#include <typeinfo>
#define RAND_MAX = 32767;
using namespace std;

vector<int> createVector(int m) {
    vector<int> V;
    for (int i = 0; i < m; i++) {
        V.emplace_back(rand());
    }
    return V;
}

void printVector(vector<int> V) {
    for (int i = 0; i < V.size(); i++) {
        cout << V[i];
    }
}

void insertionSort(vector<int>& A, int n) {
    for (int j = 1; j < n; j++) {
        int key = A[j];
        int i = j - 1;
        while ((i >= 0) && (A[i] > key)) {
            A[i + 1] = A[i];
            i = i - 1;
        }
        A[i + 1] = key;
    }
}

int left(int i) {
    return (2 * i);
}

int right(int i) {
    return ((2 * i) + 1);
}

void maxHeapify(vector<int>& A, int i, int& heap_size) {
    int largest;
    int l = left(i);
    int r = right(i);
    if ((l < heap_size) && (A[l] > A[i])) {
        largest = l;
    }
    else {
        largest = i;
    }
    if ((r < heap_size) && (A[r] > A[largest])) {
        largest = r;
    }
    if (largest != i) {
        swap(A[i], A[largest]);
        maxHeapify(A, largest, heap_size);
    }
}

void buildMaxHeap(vector<int>& A, int& heap_size) {
    heap_size = A.size();
    for (int i = A.size() / 2; i >= 0; i--) {
        maxHeapify(A, i, heap_size);
    }
}

//Passing heap_size variable by reference since vector does not contain heap_size attribute
void heapSort(vector<int>& A, int n, int& heap_size) {
    buildMaxHeap(A, heap_size);
    for (int i = n; i >= 1; i--) {
        swap(A[0], A[i]);
        heap_size--;
        maxHeapify(A, 0, heap_size);
    }
}

int partition(vector<int>& A, int p, int r) {
    int x = A[r];
    int i = p - 1;
    for (int j = p; j < r; j++) {
        if (A[j] <= x) {
            i++;
            swap(A[i], A[j]);
        }
    }
    swap(A[i + 1], A[r]);
    return i + 1;
}

int randomizedPartition(vector<int>& A, int p, int r) {
    int i = rand() % ((r - p) + 1) + p;
    swap(A[i], A[r]);
    return partition(A, p, r);
}

int randomizedSelect(vector<int>& A, int p, int r, int i) {
    if (p == r)
        return A[p];
    int q = randomizedPartition(A, p, r);
    int k = q - p + 1;
    if (i == k)
        return A[q];
    else if (i < k)
        return randomizedSelect(A, p, q - 1, i);
    else
        return randomizedSelect(A, q + 1, r, i - k);
}

void ALG1(vector<int> A, int n, int i) {
    insertionSort(A, n);
    cout << A[i - 1] << "\n";
}

void ALG2(vector<int> A, int n, int i) {
    int heap_size;
    heapSort(A, n - 1, heap_size);
    cout << A[i - 1] << "\n";
}


void ALG3(vector<int> A, int n, int i) {
    int x = randomizedSelect(A, 0, n - 1, i);
    cout << x << "\n";
}

int main(void) {
    //Set size of final vector
    int vectSize = 1000;
    double t_ALG1 = 0, t_ALG2 = 0, t_ALG3 = 0;
    //Increment by size/10 to get vectors of size 1k, 2k, ..., 10k
    for (int size = vectSize / 10; size <= vectSize; size += (vectSize / 10)) {
        //iterate over vectors of size 'size' 5 times each and use as input for ALG1, ALG2, and ALG3
        for (int m = 0; m < 5; m++) {
            vector<int> vect = createVector(size);
            int i = (2 * size) / 3;
            auto start = chrono::high_resolution_clock::now();
            ALG1(vect, size, i);
            auto end = chrono::high_resolution_clock::now();
            chrono::duration<double> elapsed_time = end - start;
            t_ALG1 += elapsed_time.count();
            start = chrono::high_resolution_clock::now();
            ALG2(vect, size, i);
            end = chrono::high_resolution_clock::now();
            elapsed_time = end - start;
            t_ALG2 += elapsed_time.count();
            start = chrono::high_resolution_clock::now();
            ALG3(vect, size, i);
            end = chrono::high_resolution_clock::now();
            elapsed_time = end - start;
            t_ALG3 += elapsed_time.count();
        }
        t_ALG1 = (t_ALG1 / 5) * 1000;
        t_ALG2 = (t_ALG2 / 5) * 1000;
        t_ALG3 = (t_ALG3 / 5) * 1000;
        cout << "____________________________________________________\n";
        cout << "The average for ALG1 at size=" << size << " is " << t_ALG1 << "ms\n";
        cout << "The average for ALG2 at size=" << size << " is " << t_ALG2 << "ms\n";
        cout << "The average for ALG3 at size=" << size << " is " << t_ALG3 << "ms\n";
        cout << "____________________________________________________\n";
        t_ALG1 = 0;
        t_ALG2 = 0;
        t_ALG3 = 0;
    }
    return 0;
}