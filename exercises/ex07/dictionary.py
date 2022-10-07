"""EX07 - Practice with Dictionary Functions."""
__author__ = "730578788"

# from exercises.ex07.dictionary import invert
def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the dictionary input."""
    invert_result: dict[str,str] = {}
    for key in dictionary:
        if dictionary[key] in invert_result:
            raise KeyError("Error: There's more than one of the same key.")
        invert_result[dictionary[key]] = key

    return invert_result


def favorite_color(name_and_colors: dict[str,str]) -> str:
    """Returns the color that appears the most frequently."""
    frequent_color: str = ""
    high_score: int = 0
    color_frequency: dict[str, int] = {}
    
    for name in name_and_colors:
        if name_and_colors[name] in color_frequency:
            color_frequency[name_and_colors[name]] += 1
        else: 
            color_frequency[name_and_colors[name]] = 1
            
    for color in color_frequency:
        if color_frequency[color] > high_score:
            high_score = color_frequency[color]
            frequent_color = color 
    return frequent_color


def count(word_list: list[str]) -> dict[str,int]:
    """Each key is a value in the given list and the values are the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for current_value in word_list:
        if current_value in result:
            result[current_value] += 1
        else:
            result[current_value] = 1
    return result



