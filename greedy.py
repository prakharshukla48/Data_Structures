pencils = [2, 9, 8, 2, 7]

# im -> index of madhav
# ir -> index of riya

im = 0
ir = len(pencils)-1

# pm -> speed of madhav
# pr -> speed of riya

pm = 0
pr = 0

while not(im == ir):
    pm = pm + 2
    pr = pr + 1
    if (pm >= pencils[im]):
        im = im + 1
        pm = pm - pencils[im]

    if (pr >= pencils[ir]):
        ir = ir - 1
        pr = pr - pencils[ir]

print ('Madhav: '+str(im+1))
print ('Riya: '+str(len(pencils)-im-1))
