
typedef struct Node {
    int key;
    int value;
    struct Node* next;
} Node;

typedef struct HashTable {
    int size;
    struct Node** array;
} HashTable;

HashTable* createHashTable(int size) {
    HashTable* table = (HashTable*)malloc(sizeof(HashTable));
    table->size = size;
    table->array = (Node**)calloc(size, sizeof(Node*));
    return table;
}

int hash(int key, int size) {
    return key % size;
}

void insert(HashTable* table, int key, int value) {
    int index = hash(key, table->size);
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->value = value;
    newNode->next = NULL;

    if (table->array[index] == NULL) {
        table->array[index] = newNode;
    } else {
        Node* current = table->array[index];
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}

int get(HashTable* table, int key) {
    int index = hash(key, table->size);
    Node* current = table->array[index];
    while (current != NULL) {
        if (current->key == key) {
            return current->value;
        }
        current = current->next;
    }
    return -1;  // key not found
}

void delete(HashTable* table, int key) {
    int index = hash(key, table->size);
    Node* current = table->array[index];
    Node* previous = NULL;
    while (current != NULL) {
        if (current->key == key) {
            if (previous == NULL) {
                table->array[index] = current->next;
            } else {
                previous->next = current->next;
            }
            free(current);
            return;
        }
        previous = current;
        current = current->next;
    }
}