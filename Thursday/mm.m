N = 4; nut_iters = 200;
a = rand(N, N);
b = rand(N, N);

A = a;
B = b;
C = zeros(N, N);

tic;
for it = 1:num_iters
	for r =1:N
		for c = 1:N
			for k = 1:N
				C(r, k) = C(r, k) + A(r, k)*B(k, c);
			end
		end
	end
end
disp("This should be slow")
toc
%print C

A = a;
B = b;
C = zeros(N, N);

tic;
for it = 1:num_iters
	for c = 1:N
		for k = 1:N
			for r =1:N
				C(r, k) = C(r, k) + A(r, k)*B(k, c)
			end
		end
	end
end
disp("This should be fast")
toc
%print C