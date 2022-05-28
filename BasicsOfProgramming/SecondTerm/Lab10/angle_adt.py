"""
Angle Abstract data type
"""


class AngleADT:
    """
    Angle ADT
    """

    def encode_message(self, senten):
        """
        Encodes the message
        >>> angle = AngleADT()
        >>> angle.encode_message("hello")
        [135.0, 45.0, -45.0, -22.5, 22.5, 135.0, -135.0, 135.0, -135.0, 202.5]
        """
        cur_angle = 0
        rotation_seq = []
        for converted in senten:
            nums = self.convert_to_num(converted)
            for num in nums:
                agl = self.num_to_angle(num)
                if agl == cur_angle:
                    rotation_seq.append(360.0)
                else:
                    rotation_seq.append(agl - cur_angle)
                    cur_angle = agl
        return rotation_seq

    def num_to_angle(self, num):
        """
        Numerates the angle
        >>> angle = AngleADT()
        >>> angle.num_to_angle(2)
        45
        """
        return num * 22.5

    def convert_to_num(self, converted, fill=2):
        """
        Convertes a char to num
        >>> angle = AngleADT()
        >>> angle.convert_to_num("d")
        [6, 4]
        """
        encoded = hex(ord(converted))[2:]
        if len(encoded) < 3:
            encoded = encoded.rjust(fill, '0')
        else:
            encoded = encoded.rjust(3, '0')
        nums = []
        for elem in encoded:
            if elem in 'abcdef':
                elem = ord(elem) - ord('a') + 10
            else:
                elem = int(elem)
            nums.append(elem)
        return nums
