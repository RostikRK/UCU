"""
Polynomial class
"""
class Polynomial:
    """
    Polynomial class
    """
    # Create a new polynomial object.
    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._poly_head = None
        else:
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    # Return the degree of the polynomial.
    def degree(self):
        """
        Returns degree of node
        """
        if self._poly_head is None:
            return -1
        else:
            return self._poly_head.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        cur_node = self._poly_head
        while cur_node is not None and cur_node.degree != degree:
            cur_node = cur_node.next

        if cur_node is None or cur_node.degree != degree:
            return 0.0
        else:
            return cur_node.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        """
        evaluates by argument
        """
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        cur_node = self._poly_head
        while cur_node is not None:
            result += cur_node.coefficient * (scalar ** cur_node.degree)
            cur_node = cur_node.next
        return result

    # Polynomial addition: newPoly = self + rhs_poly.
    def __add__(self, rhs_poly):
        new_poly = self.reduce(rhs_poly)
        return new_poly

    # Polynomial subtraction: newPoly = self - rhs_poly.
    def __sub__(self, rhs_poly):
        new_poly = self.reduce(rhs_poly, reduce=lambda x, y: x-y)
        return new_poly

    # Polynomial multiplication: newPoly = self * rhs_poly.
    def __mul__(self, rhs_poly):
        count = 0
        current = self._poly_head
        while current != None:
            current2 = rhs_poly._poly_head
            temp_poly = Polynomial()
            while current2 != None:
                coef = current.coefficient * current2.coefficient
                degr = current.degree + current2.degree
                temp_poly._append_term(degr, coef)
                current2 = current2.next
            if count == 0:
                new_poly = temp_poly
                count += 1
            else:
                new_poly = new_poly.reduce(temp_poly)
            current = current.next
        return new_poly


    def reduce(self, rhs_poly, reduce=None):
        """
        Calculates adding and sub 
        """
        reduce = reduce or (lambda x, y: x+y)
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()
        else:
            max_degree = rhs_poly.degree()

        i = max_degree
        while i >= 0:
            value = reduce(self[i], rhs_poly[i])
            new_poly._append_term(i, value)
            i -= 1
        return new_poly

    def _append_term(self, degree, coefficient):
        if coefficient != 0.0:
            new_term = _PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

    def __str__(self):
        pass


# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.coefficient) + "x^" + str(self.degree)
