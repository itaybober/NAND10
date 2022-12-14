"""
This file is part of nand2tetris, as taught in The Hebrew University, and
was written by Aviv Yaish. It is an extension to the specifications given
[here](https://www.nand2tetris.org) (Shimon Schocken and Noam Nisan, 2017),
as allowed by the Creative Common Attribution-NonCommercial-ShareAlike 3.0
Unported [License](https://creativecommons.org/licenses/by-nc-sa/3.0/).
"""
import typing


class SymbolTable:
    """A symbol table that associates names with information needed for Jack
    compilation: type, kind and running index. The symbol table has two nested
    scopes (class/subroutine).
    """

    def __init__(self) -> None:
        """Creates a new empty symbol table."""
        self.class_table = {"STATIC": [], "FIELD": []}
        self.subroutine_table = {}

    def __str__(self):
        return "class table: " + str(self.class_table) + "\n" + "sub_table: " + str(self.subroutine_table)



    def start_subroutine(self) -> None:
        """Starts a new subroutine scope (i.e., resets the subroutine's 
        symbol table).
        """
        self.subroutine_table = {"VAR": [], "ARG": []}


    def define(self, name: str, type: str, kind: str) -> None:
        """Defines a new identifier of a given name, type and kind and assigns 
        it a running index. "STATIC" and "FIELD" identifiers have a class scope, 
        while "ARG" and "VAR" identifiers have a subroutine scope.

        Args:
            name (str): the name of the new identifier.
            type (str): the type of the new identifier.
            kind (str): the kind of the new identifier, can be:
            "STATIC", "FIELD", "ARG", "VAR".
        """
        if kind == "FIELD":
            self.class_table["FIELD"].append((name, type))
        elif kind == "STATIC":
            self.class_table["STATIC"].append((name, type))
        elif kind == "VAR":
            self.subroutine_table["VAR"].append((name, type))
        else:
            self.subroutine_table["ARG"].append((name, type))



    def var_count(self, kind: str) -> int:
        """
        Args:
            kind (str): can be "STATIC", "FIELD", "ARG", "VAR".

        Returns:
            int: the number of variables of the given kind already defined in 
            the current scope.
        """
        if kind in ["STATIC", "FIELD"]:
            return len(self.class_table[kind])
        return len(self.subroutine_table[kind])

    def kind_of(self, name: str) -> str:
        """
        Args:
            name (str): name of an identifier.

        Returns:
            str: the kind of the named identifier in the current scope, or None
            if the identifier is unknown in the current scope.
        """
        for (var_name, var_type) in self.subroutine_table["ARG"]:
            if var_name == name:
                return "ARG"
        for (var_name, var_type) in self.subroutine_table["VAR"]:
            if var_name == name:
                return "VAR"
        for (var_name, var_type) in self.class_table["STATIC"]:
            if var_name == name:
                return "STATIC"
        return "FIELD"


    def type_of(self, name: str) -> str:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            str: the type of the named identifier in the current scope.
        """
        for (var_name, type) in self.class_table["STATIC"]:
            if var_name == name:
                return type
        for (var_name, type) in self.class_table["FIELD"]:
            if var_name == name:
                return type
        for (var_name, type) in self.subroutine_table["ARG"]:
            if var_name == name:
                return type
        for (var_name, type) in self.subroutine_table["VAR"]:
            if var_name == name:
                return type


    def index_of(self, name: str) -> int:
        """
        Args:
            name (str):  name of an identifier.

        Returns:
            int: the index assigned to the named identifier.
        """
        # Your code goes here!
        index = 0
        for (var_name, var_type) in self.subroutine_table["ARG"]:
            if var_name == name:
                return index
            index += 1
        index = 0
        for (var_name, var_type) in self.subroutine_table["VAR"]:
            if var_name == name:
                return index
            index += 1
        index = 0
        for (var_name, var_type) in self.class_table["STATIC"]:
            if var_name == name:
                return index
            index += 1
        index = 0
        for (var_name, var_type) in self.class_table["FIELD"]:
            if var_name == name:
                return index
            index += 1
