#!/usr/bin/env python

bowtie2-build -fa chr19.fa chr19

bowtie2 -x chr19 -U CTCF_ER4.fastq -S CTCF_ER4.sam
bowtie2 -x chr19 -U CTCF_G1E.fastq -S CTCF_G1E.sam
bowtie2 -x chr19 -U input_ER4.fastq -S input_ER4.sam
bowtie2 -x chr19 -U input_G1E.fastq -S input_G1E.sam

macs2 callpeak -t CTCF_ER4.sam -g 61000000 -c input_ER4.sam -n "ER4cont" --outdir "/Users/cmdb/qbb2017-answers/week6/ER4cont"
macs2 callpeak -t CTCF_ER4.sam -g 61000000 -n "ER4" --outdir "/Users/cmdb/qbb2017-answers/week6/ER4"
macs2 callpeak -t CTCF_G1E.sam -g 61000000 -c input_G1E.sam -n "G1Econt" --outdir "/Users/cmdb/qbb2017-answers/week6/G1Econt"
macs2 callpeak -t CTCF_G1E.sam -g 61000000 -n "G1E" --outdir "/Users/cmdb/qbb2017-answers/week6/G1E"

bedtools intersect -a "/Users/cmdb/qbb2017-answers/week6/ER4cont/ER4cont_peaks.narrowPeak" -b "/Users/cmdb/qbb2017-answers/week6/G1Econt/G1Econt_peaks.narrowPeak" -v > ER4cont_uniq.bed
bedtools intersect -a "/Users/cmdb/qbb2017-answers/week6/G1Econt/G1Econt_peaks.narrowPeak" -b "/Users/cmdb/qbb2017-answers/week6/ER4cont/ER4cont_peaks.narrowPeak"  -v > G1Econt_uniq.bed
bedtools intersect -a "/Users/cmdb/qbb2017-answers/week6/ER4/ER4_peaks.narrowPeak" -b "/Users/cmdb/qbb2017-answers/week6/G1E/G1E_peaks.narrowPeak" -v > ER4_uniq.bed
bedtools intersect -a "/Users/cmdb/qbb2017-answers/week6/G1E/G1E_peaks.narrowPeak" -b "/Users/cmdb/qbb2017-answers/week6/ER4/ER4_peaks.narrowPeak" -v > G1E_uniq.bed

head -100 ER4cont_uniq.bed > ER4cont_uniq_short.bed
head -100 G1Econt_uniq.bed > G1Econt_uniq_short.bed
head -100 ER4_uniq.bed > ER4_uniq_short.bed
head -100 G1E_uniq.bed > G1E_uniq_short.bed

#For motif binding, need to sort by signalValue and choose top 100 from narrowpeak file of ER4 and ER4cont only

sort -k 7 -r -n ER4cont_uniq.bed > ER4cont_uniq_sorted.bed
sort -k 7 -r -n ER4_uniq.bed > ER4_uniq_sorted.bed
sort -k 7 -r -n G1Econt_uniq.bed > G1Econt_uniq_sorted.bed
sort -k 7 -r -n G1E_uniq.bed > G1E_uniq_sorted.bed

head -100 ER4cont_uniq_sorted.bed > ER4cont_uniq_sorted_short.bed
head -100 ER4_uniq_sorted.bed > ER4_uniq_sorted_short.bed
head -100 G1Econt_uniq_sorted.bed > G1Econt_uniq_sorted_short.bed
head -100 G1E_uniq_sorted.bed > G1E_uniq_sorted_short.bed

bedtools getfasta -fi chr19.fa -bed ER4cont_uniq_sorted_short.bed -name -fo ER4cont_uniq_sorted_short.fa
bedtools getfasta -fi chr19.fa -bed ER4_uniq_sorted_short.bed -name -fo ER4_uniq_sorted_short.fa
bedtools getfasta -fi chr19.fa -bed G1Econt_uniq_sorted_short.bed -name -fo G1Econt_uniq_sorted_short.fa
bedtools getfasta -fi chr19.fa -bed G1E_uniq_sorted_short.bed -name -fo G1E_uniq_sorted_short.fa

/usr/local/opt/meme/bin/meme-chip -meme-maxw 20 -o ER4cont_out -db /Users/cmdb/qbb2017-answers/week6/motif_databases/JASPAR/JASPAR_CORE_2016.meme ER4cont_uniq_sorted_short.fa
/usr/local/opt/meme/bin/meme-chip -meme-maxw 20 -o ER4_out -db /Users/cmdb/qbb2017-answers/week6/motif_databases/JASPAR/JASPAR_CORE_2016.meme ER4_uniq_sorted_short.fa
/usr/local/opt/meme/bin/meme-chip -meme-maxw 20 -o G1Econt_out -db /Users/cmdb/qbb2017-answers/week6/motif_databases/JASPAR/JASPAR_CORE_2016.meme G1Econt_uniq_sorted_short.fa
/usr/local/opt/meme/bin/meme-chip -meme-maxw 20 -o G1E_out -db /Users/cmdb/qbb2017-answers/week6/motif_databases/JASPAR/JASPAR_CORE_2016.meme G1E_uniq_sorted_short.fa

git add ER4cont_uniq_sorted_short.bed ER4_uniq_sorted_short.bed G1Econt_uniq_sorted_short.bed G1E_uniq_sorted_short.bed 
git add ./ER4cont_out/meme_out/logo_rc1.pdf ./ER4_out/meme_out/logo_rc1.pdf ./G1Econt_out/meme_out/logo_rc1.pdf ./G1E_out/meme_out/logo_rc1.pdf
git add ./ER4cont_out/meme_out/meme.html ./ER4_out/meme_out/meme.html ./G1Econt_out/meme_out/meme.html ./G1E_out/meme_out/meme.html
git add ER4cont_locations.txt ER4_locations.txt G1Econt_locations.txt G1E_locations.txt
git add mapreads.py
