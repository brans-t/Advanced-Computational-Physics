# 随机抽样法-Gauss分布
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.special import erfinv

np.random.seed()
mu, sigma = 0, 1
n = 10000
samples = []
############1#直接抽样法（反函数法）###############################
#高斯分布随机数的抽样函数（反函数）
def Inverse_functions_Gauss(mu, sigma, n):
    uniform_numbers = np.random.rand(n)                               #生成均匀分布的随机数
    Gauss = mu + sigma * np.sqrt(2) * erfinv(2 * uniform_numbers - 1) #使用高斯分布的反函数对均匀分布随机数进行转换
    return Gauss
data1 = Inverse_functions_Gauss(mu, sigma, n)

############2#变换抽样法##########################################
#高斯分布随机数的抽样函数
def transform_functions_Gauss(mu, sigma, n):
    #生成两组均匀分布的随机数
    u = np.random.rand(n)
    v = np.random.rand(n)
    # 使用Box-Muller变换生成标准正态分布的随机数
    x = np.sqrt(-2 * np.log(u)) * np.cos(2 * np.pi * v)
    y = np.sqrt(-2 * np.log(u)) * np.sin(2 * np.pi * v)
    Gauss = mu + sigma * x
    return Gauss
data2 = transform_functions_Gauss(mu, sigma, n)

############3#舍选抽样法##########################################
#定义目标分布函数（Gauss）
def target_functions_Gauss(x, mu, sigma):
    return 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
#定义均匀分布抽样函数
def uniform_numbers(a, b, n):
    return np.random.uniform(a, b, n)
#舍选抽样
def rejection_numbers(mu, sigma, n):
    max_pdf = target_functions_Gauss(mu, mu, sigma)  # 目标分布的最大概率密度
    while len(samples) < n:
        x = uniform_numbers(mu - 3 * sigma, mu + 3 * sigma, 1)  # 在均匀分布范围内抽样
        y = uniform_numbers(0, max_pdf, 1)                      #在0到目标分布最大概率密度之间抽样
        if y <= target_functions_Gauss(x, mu, sigma):
            samples.append(x)
    return np.array(samples)
data3 = rejection_numbers(mu, sigma, n)

################4#中心极限定理####################################
# 生成符合均匀分布的随机数并计算其均值和标准差
m = 100
uniform_numbers = np.random.uniform(0, 1, (n, m))
means = np.mean(uniform_numbers, axis=1)   #计算每次抽样的均值
stds = np.std(uniform_numbers, axis=1)     #计算每次抽样的标准差
data4 = (means - 0.5) / (1 / np.sqrt(12))  #生成高斯分布随机数

################5#第二类舍选法######################################
# 定义高斯分布的概率密度函数
def gaussian(x, mu, sigma):
    return 1 / (np.sqrt(2 * np.pi) * sigma) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
#生成符合高斯分布的随机数
def acceptance_rejection_Gauss(mu, sigma, n):
    while len(samples) < n:
        x = np.random.uniform(-5 * sigma + mu, 5 * sigma + mu)   #从较宽的均匀分布中随机抽取一个点
        u = np.random.rand()                                     #生成在提议分布下的均匀抽样点
        #如果在目标分布下的概率密度比例大于在提议分布下的概率密度比例，则接受
        if u < gaussian(x, mu, sigma) / (2 * gaussian(mu, mu, sigma)):
            samples.append(x)
    return np.array(samples)
data5 = acceptance_rejection_Gauss(mu, sigma, n)

########################高斯分布################################
data = np.random.normal(mu, sigma, 1000)
# 绘制高斯分布的概率密度函数
x = np.linspace(-4, 4, 1000)
data6 = 1/(np.sqrt(2*np.pi)*sigma) * np.exp(-(x - mu)**2 / (2*sigma**2))

#绘图
plt.hist(data1, bins=30, density=True, alpha=0.6, color='blue')
plt.hist(data2, bins=30, density=True, alpha=0.6, color='red')
plt.hist(data3, bins=30, density=True, alpha=0.6, color='orange')
plt.hist(data4, bins=30, density=True, alpha=0.6, color='black')
plt.hist(data5, bins=30, density=True, alpha=0.6, color='purple')
plt.plot(x, data6, color='black', linewidth=2, linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.show()