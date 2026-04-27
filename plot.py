import numpy as np
import matplotlib.pyplot as plt

def load_values(path):
    vals = []
    with open(path, 'r') as f:
        lines = f.readlines()[1:]
        for x in lines:
            parts = x.strip().split()
            vals.append(float(parts[1]))
    return np.array(vals)

iou_Edge = load_values('./result/iou_EdgeDetec.txt')
f1_Edge  = load_values('./result/f1_EdgeDetec.txt')

iou_Th   = load_values('./result/iou_ThreshSeg.txt')
f1_Th    = load_values('./result/f1_ThreshSeg.txt')
#F1对比
plt.figure(1)

plt.hist(f1_Edge, bins=20,alpha=0.5,label='Edge F1')
plt.hist(f1_Th,  bins=20,alpha=0.5,label='Threshold F1')

plt.xlabel('F1 score')
plt.ylabel('Count')
plt.title('F1 Distribution')
plt.legend()
plt.grid()

plt.show()

#IOU分布
plt.figure(2)

plt.hist(iou_Edge, bins=20, alpha=0.5, label='Edge')
plt.hist(iou_Th, bins=20, alpha=0.5, label='Threshold')

plt.xlabel('IoU')
plt.ylabel('Count')
plt.title('IoU Distribution')
plt.legend()

plt.show()

#箱线图
plt.figure(3)

plt.boxplot([iou_Edge, iou_Th],
            labels=['Edge', 'Threshold'])

plt.title('IoU Boxplot')
plt.ylabel('IoU')

plt.show()

#均值对比
print("Edge IoU mean:", np.mean(iou_Edge))
print("Threshold IoU mean:", np.mean(iou_Th))

print("Edge F1 mean:", np.mean(f1_Edge))
print("Threshold F1 mean:", np.mean(f1_Th))