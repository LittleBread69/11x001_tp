# All there is to know about pointers in C

## Definition and why should one use them

A pointer is a type of a value that points to an adress in a memory.

```C
int integer;
float floating_point;
int *pointer_to_int;
int **pointer_to_pointer_of_int;
```

## When to use `*` and `&`

```C
//declaration
int *pointer;

//reference - telling a pointer to point to an adress
int variable = 0;
int *pointer = &variable; //points to the adress of variable

//deference - working with the value present at where the pointer is pointing to
*variable += 7;
*variable *= *variable; //here we are multiplying with the value of variable
*variable -= 7;
```

## Typical usecases

### Dynamically allocated arrays

Example
```C
//code that prints the values of a dynamically allocated array
int *array = malloc(sizeof(int) * 4);
for (int i = 0; i < 4; i++){
    printf("%d\n", array[i]);
}
```


### Return multiple values

In `Python`, if you want to return multiple values, you'd do something like this:
```python
def return_multiple_values(*args):
    var1, var2, var3 = args
    var1 = 5
    var2 = 3
    var3 = 110
    return var1, var2, var3
```

In `C`, it's different:
```C
void return_numbers(int* var1, int *var2, int * var3){ //note the equivalent but different notations
    *var1 = 5;
    *var2 = 3;
    *var3 = 110;
    //there's no need to return, all the value are changed
}
```

### Apply OOP principles in C

```C
#include <stdlib.h>
#include <stdio.h>

typedef struct _car{
    int wheelCount;
    char *brand; //pointer to char array that finishes with '\0' aka a 'string'
    float speed;
} t_car;

void setCarValues(t_car *car, int wheelCount, char *brand, float speed){
    car->wheelCount = wheelCount;
    car->brand = brand;
    
    //equivalent
    car->speed = speed;
    (*car).speed = speed;

    //why use one or the other when setting values
    t_car *carArray = malloc(sizeof(car) * 3);
    //equivalent
    carArray[2].wheelCount = 5;
    t_car vehicle = carArray[2]; vehicle.wheelCount = 5;
    (carArray + 2 * sizeof(car))->wheelCount = 5;
}

t_car makeNewCar(int wheelCount, char *brand, float speed){
    t_car vehicle;
    vehicle.wheelCount = wheelCount;
    vehicle.brand = brand;
    vehicle.speed = speed;
    return vehicle;
}
```