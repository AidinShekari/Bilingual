# latexmk configuration for Advanced Communication Networks
# XeLaTeX -> XDV -> PDF, with biber for biblatex bibliographies.
$pdf_mode        = 5;      # xelatex
$dvi_mode        = 0;
$postscript_mode = 0;
$xelatex  = 'xelatex -interaction=nonstopmode -halt-on-error -file-line-error %O %S';
$bibtex_use      = 2;      # run biber when needed, delete .bbl on clean
$biber           = 'biber %O %S';  # keep INFO output: latexmk parses it
$max_repeat      = 6;      # cover TOC + cleveref + biblatex need several passes
$silent          = 1;
@default_files   = ();

# The shared bibliography lives in references/; make it visible to biber and
# to latexmk's dependency check through BIBINPUTS (no paths in the .tex files).
use File::Basename qw(dirname);
use Cwd qw(abs_path);
my $acn_root = dirname(abs_path(__FILE__));
$ENV{'BIBINPUTS'} = "$acn_root/references//:" . ($ENV{'BIBINPUTS'} // '');
