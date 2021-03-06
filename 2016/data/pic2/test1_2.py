##############################################################################

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

##############################################################################

workspace = '/Users/yuki/survey/workspace/2016/data/pic2/'
fig_home = '{}outline/'.format(workspace)

data_logs = ['{}20/sda.log'.format(workspace),
             '{}26/sda.log'.format(workspace)]

##############################################################################

plt.style.use('ggplot')
plt.figure(figsize=(8,6))
plt.ylabel('mean loss')
plt.xlabel('epoch')

for log in data_logs:
    f = open(log, mode='r')
    lines = f.readlines()
    f.close()
    test_loss = [list(map(float, line.split()))[2] for line in lines]

    plt.plot(range(len(test_loss)), test_loss)
    plt.plot()

fp = FontProperties(fname='/Library/Fonts/Microsoft/MS Gothic.ttf', size=14)
plt.legend(['実験1','実験2','実験3'], prop=fp, loc='best')
plt.savefig('{}loss5_2.png'.format(fig_home), bbox_inches='tight', pad_inches=0.0)
plt.close()

##############################################################################
