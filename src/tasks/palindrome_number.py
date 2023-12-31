

class PalindromeNumberSolution:

    @staticmethod
    def is_palindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x % 10 == 0 and x != 0:
            return False
        num_str = str(x)
        reverse_str = num_str[::-1]
        if len(num_str) == 1:
            return True
        if num_str == reverse_str:
            return True
        return False


class TestPalindromeNumberSolution:

    def test_simple_number(self):
        assert PalindromeNumberSolution.is_palindrome(121) is True

    def test_negative_number(self):
        assert PalindromeNumberSolution.is_palindrome(-121) is False

    def test_zero_number(self):
        assert PalindromeNumberSolution.is_palindrome(0) is True

    def test_number_negative_case(self):
        assert PalindromeNumberSolution.is_palindrome(123) is False
