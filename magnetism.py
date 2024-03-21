def calc_e_field(q, r):
    """
    Calculates the charge that would be experienced at r distance, given q charge

    Parameters:
    q - num
        (coulombs) the electric charge
    r - num
        (meters) the distance to the point which you wish to find the field from q

    Returns:
    e_field - float
        charge in coulombs
    """
    k = 8.99e9
    e_field = (k * q) / r**2
    return e_field

if __name__ == "__main__":
    pass