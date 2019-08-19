clear all
data = xlsread('input_data.xlsx');
size_data = size(data);
raw = size_data(1);
cow = size_data(2);
fs = 1/(30*60);
for i  = 3:1:10
    testcase = data(1, i);
    emu = data(2:end, i);
    emu = emu(~isnan(emu));
    hd = figure(i);
    subplot(2,1,1)
    L = length(emu);
    freq = (0:1:(L-1))/(L-1)*fs;
    plot(freq, abs(fft(emu - mean(emu))))
    xlabel('frequency')
    ylabel('amplitude')
    title('FFT')
    
    subplot(2,1,2)
    t = (0:1:(L-1))/2;
    plot(t, emu, 'b')
    xlabel('Time(hour)')
    ylabel('Amplitude')
    hold on
    
    [C, L] = wavedec(emu, 4,  'db5');
    approx = appcoef(C, L, 'db5');
    [cd1, cd2, cd3, cd4] = detcoef(C, L, [1 2 3 4]);
    new_C = [approx; 0*cd4; 0*cd3; 0*cd2; 0*cd1];
    new_emu = waverec(new_C, L, 'db5');
    plot(t, new_emu, 'r')
    hold off
    legend('original', 'reconstruction by db5');
    %filename = strcat(string(i), 'ret.fig');
    %savefig(hd, 'ret.fig')
    fn = sprintf('%d_ret_fft_reconstruct.png', i);
    saveas(gcf, fn)
    %saveas(hd, filename);
    
end



