fx = @(x, y) y - 2*x/y;

% 初始条件
x0 = 0;
y0 = 1;

% 范围
xspan = [0 16];

% 求解常微分方程
[x, y] = ode45(fx, xspan, y0);

% 绘制图形
plot(x, y, 'LineWidth', 1.5);
xlabel('x');
ylabel('y');
title('Solution of dy/dx = y - 2*x/y with initial condition (0, 1)');
grid on;
