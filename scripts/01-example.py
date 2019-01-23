#!/usr/bin/env python

import pandastoproduction as p2p

site = p2p.Site(slug='example-site')

s1 = p2p.Scatterplot()
p1 = p2p.Paragraph('This scatterplot shows an interesting trend...')

page1 = p2p.Page('Page 1 Title', content=[s1, p1])

h1 = p2p.Histogram()
p2 = p2p.Paragraph('This histogram shows...')
b1 = p2p.Boxplot()
p2 = p2p.Paragraph('This boxplot shows...')

page2 = p2p.Page('Page 2 Title', content=[h1, p2, b1, p2])

# TODO associate page(s) with site

# TODO include dataframes

# TODO include parameters to charts, dataframes, etc

p2p.publish(pages=[page1, page2], sites=[site])
