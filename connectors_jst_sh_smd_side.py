#!/usr/bin/env python

import argparse
from kicad_mod import KicadMod, createNumberedPadsSMD

parser = argparse.ArgumentParser()
parser.add_argument('pincount', help='number of pins of the jst connector', type=int, nargs=1)
parser.add_argument('-v', '--verbose', help='show extra information while generating the footprint', action='store_true') #TODO
args = parser.parse_args()

# http://www.jst-mfg.com/product/pdf/eng/eSH.pdf

pincount = int(args.pincount[0])

pad_spacing = 1.
start_pos_x = -(pincount-1)*pad_spacing/2.
end_pos_x = (pincount-1)*pad_spacing/2.

# SMT type shrouded header, Top entry type
footprint_name = 'Connectors_JST_SM{pincount:02g}B-SRSS-TB'.format(pincount=pincount)

kicad_mod = KicadMod(footprint_name)
kicad_mod.setDescription("JST SH series connector, SM{pincount:02g}B-SRSS-TB".format(pincount=pincount))
kicad_mod.setAttribute('smd')
kicad_mod.setCenterPos({'x':0, 'y':3.875/2})

# set general values
kicad_mod.addText('reference', 'CON**', {'x':start_pos_x, 'y':-2}, 'F.SilkS')
kicad_mod.addText('value', footprint_name, {'x':0, 'y':6.2}, 'F.Fab')

# create Silkscreen

kicad_mod.addLine({'x':start_pos_x-0.4, 'y':4.575}, {'x':end_pos_x+0.4, 'y':4.575}, 'F.SilkS', 0.15)

'''
kicad_mod.addPolygoneLine([{'x':start_pos_x+0.5, 'y':4.575}
                          ,{'x':start_pos_x+0.5, 'y':4.575-1}
                          ,{'x':end_pos_x-0.5, 'y':4.575-1}
                          ,{'x':end_pos_x-0.5, 'y':4.575}]
                          ,'F.SilkS', 0.15)
'''

kicad_mod.addPolygoneLine([{'x':start_pos_x-1.5, 'y':3.875-1.2}
                          ,{'x':start_pos_x-1.5, 'y':4.575-4.25}
                          ,{'x':start_pos_x-0.6, 'y':4.575-4.25}]
                          ,'F.SilkS', 0.15)

kicad_mod.addRectLine({'x':start_pos_x-1, 'y':4.575-4.25}, {'x':start_pos_x-1, 'y':4.575-4.25+1.2}, 'F.SilkS', 0.15)
kicad_mod.addRectLine({'x':start_pos_x-1, 'y':4.575-4.25+0.5}, {'x':start_pos_x-1.5, 'y':4.575-4.25+0.5}, 'F.SilkS', 0.15)
kicad_mod.addRectLine({'x':start_pos_x-1, 'y':4.575-4.25+1.2}, {'x':start_pos_x-1.5, 'y':4.575-4.25+1.2}, 'F.SilkS', 0.15)

kicad_mod.addPolygoneLine([{'x':end_pos_x+1.5, 'y':3.875-1.2}
                          ,{'x':end_pos_x+1.5, 'y':4.575-4.25}
                          ,{'x':end_pos_x+0.6, 'y':4.575-4.25}]
                          ,'F.SilkS', 0.15)

kicad_mod.addRectLine({'x':end_pos_x+1, 'y':4.575-4.25}, {'x':end_pos_x+1, 'y':4.575-4.25+1.2}, 'F.SilkS', 0.15)
kicad_mod.addRectLine({'x':end_pos_x+1, 'y':4.575-4.25+0.5}, {'x':end_pos_x+1.5, 'y':4.575-4.25+0.5}, 'F.SilkS', 0.15)
kicad_mod.addRectLine({'x':end_pos_x+1, 'y':4.575-4.25+1.2}, {'x':end_pos_x+1.5, 'y':4.575-4.25+1.2}, 'F.SilkS', 0.15)

kicad_mod.addCircle({'x':start_pos_x-1, 'y':-0.25}, {'x':0.25, 'y':0}, 'F.SilkS', 0.15)

# create Courtyard
kicad_mod.addRectLine({'x':start_pos_x-0.7-1.2-0.25, 'y':4.775+0.25+0.0125}, {'x':end_pos_x+0.7+1.2+0.25, 'y':-0.775-0.25-0.0375}, 'F.CrtYd', 0.05)

# create pads
createNumberedPadsSMD(kicad_mod, pincount, pad_spacing, {'x':0.6, 'y':1.55}, 0)
kicad_mod.addPad('""', 'smd', 'rect', {'x':start_pos_x-0.7-1.2/2, 'y':3.875}, {'x':1.2, 'y':1.8}, 0, ['F.Cu', 'F.Paste', 'F.Mask'])
kicad_mod.addPad('""', 'smd', 'rect', {'x':end_pos_x+0.7+1.2/2, 'y':3.875}, {'x':1.2, 'y':1.8}, 0, ['F.Cu', 'F.Paste', 'F.Mask'])

# save model
kicad_mod.save('{footprint_name}.kicad_mod'.format(footprint_name=footprint_name))