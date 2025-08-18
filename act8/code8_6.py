import plotly.express as px
import webbrowser
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../data/GNI2014.csv')
df.head()

fig = px.treemap(data_frame = df, 
    path = ['continent', 'iso3'],
    values = 'population',
    color = 'GNI',
    color_continuous_scale = 'Bluyl',)
plt.axis('off')
fig.update_layout(margin_t = 0, margin_l = 0, margin_r = 0, margin_b = 0,
                  width = 800, height = 600,
                  title_text = 'GNI 2014',
                  title_font_size = 20,)
# fig.write_html('C://Users/benjie/Desktop/python/data/treemap.html')
# webbrowser.open('C://Users/benjie/Desktop/python/data/treemap.html')
import matplotlib.image as mpimg
fig.write_image('treemap.png')
plt.imshow(mpimg.imread('treemap.png'))
plt.axis('off')
plt.show()

# fig.update_layout(margin_t=)