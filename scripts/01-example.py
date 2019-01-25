#!/usr/bin/env python

import pandas as pd
import pandastoproduction as p2p

df = pd.DataFrame({
    'Name': ['Bob', 'Donald', 'Sue', 'Gregory'],
    'Age': [43, 71, 38, 25],
})

df1 = p2p.DataFrame(df)

s1 = p2p.Scatterplot()
p1 = p2p.Paragraph('This scatterplot shows an interesting trend...')

page1 = p2p.Page('Page 1 Title', content=[s1, p1])
p2p.show(page1)

h1 = p2p.Histogram()
p2 = p2p.Paragraph('This histogram shows...')
b1 = p2p.Boxplot()
p2 = p2p.Paragraph('This boxplot shows...')

page2 = p2p.Page('Page 2 Title', content=[h1, p2, b1, p2])
p2p.show(page2)

p2p.publish(pages=[page1, page2], dataframes=[df1])
