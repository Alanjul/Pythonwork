from DeckOfCards import DeckOfCard
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib.image as mpimg #loading images
#building a path
path = Path('.').joinpath('card_images')

deck_of_cards = DeckOfCard()
#returns the tuples of figures, and axes object
figure, axes_list = plt.subplots(nrows=4, ncols=13)

#iterate through the subplots
#ravel() to iterate the list as one dimension
deck_of_cards.shuffle()
for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False) #hide the x axis
    axes.get_yaxis().set_visible(False) #hid the y axis
    name_image =  deck_of_cards.deal_card().name_image #to get the file name
    #append the path the image name with resolve
    # to find the full path and return it as a string
    img = mpimg.imread(str(path.joinpath(name_image).resolve()))
    axes.imshow(img) #display the image

