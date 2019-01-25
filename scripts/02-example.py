#!/usr/bin/env python

import pandas as pd
import pandastoproduction as p2p

df = pd.DataFrame({
    'Name': ['Bob', 'Donald', 'Sue', 'Gregory'],
    'Age': [43, 71, 38, 25],
    'Income': [100, 40, 22, 19],
    'Group': [1, 1, 2, 2],
})

df1 = p2p.DataFrame(df)

s1 = p2p.Scatterplot('Income', 'Age')

s1.title = 'title for s1'
# i would kind of prefer it to be s1.title('this is the title')...

p1 = p2p.Paragraph('This scatterplot shows an interesting trend...')

page1 = p2p.Page('Page 1 Title', content=[s1, p1])

h1 = p2p.Histogram(series='Age')
p2 = p2p.Paragraph('This histogram shows...')


b1 = p2p.Boxplot('Income', grouping='Group')
p2 = p2p.Paragraph('This boxplot shows...')

page2 = p2p.Page('Page 2 Title', content=[h1, p2, b1, p2])

p2p.publish(pages=[page1, page2], dataframes=[df1])
