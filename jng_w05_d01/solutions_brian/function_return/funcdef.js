var methodName = process.argv[2];

var methodDefinitions = {
    "push": "Appends a value to the end of a array",
    "splice": "Method has three parameters: start, deletecount, and itemN. The method deletes delecount items starting at start, and then inserts itemN into the list at start",
    "length": "Returns the length of an array" ,
    "typeOf": "Returns a string representing the object of primitive type (ie: string, number)",
    "reverse": "reverses an array in place",
    "sort": "sorts an array in place (in string order, so 10 comes before 2)",
    "toString": "returns a string representation of an object or primitive datatype",
    "indexOf": "takes in a value, and returns the first index in the array where that value is found. Returns -1 if value is not found.",
    "shift": "removes the first element from an array and returns it",
    "concat": "takes the array the method is called on as well as another that is passed in as an argument, and returns a new array that is a concatenation of both",
    "forEach": "executes the provided function, once for each array element",
    "join": "takes in a string, and then returns a concatenation of all array elements as one large string, with the passed in argument as a delimiter",
    "slice": "takes in two arguments: begin and end. The method returns a copy of an array, but only the elements starting at begin and ending at end",
    "fill": "takes in 3 arguments: the fill value, start and end. The method will alter an array so that it replaces the value at every index from start to end with the fill value."
};

console.log(methodName + ": " + methodDefinitions[methodName]);
