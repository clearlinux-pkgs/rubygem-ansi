#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ansi
Version  : 1.5.0
Release  : 8
URL      : https://rubygems.org/downloads/ansi-1.5.0.gem
Source0  : https://rubygems.org/downloads/ansi-1.5.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : ruby
BuildRequires : rubygem-ae
BuildRequires : rubygem-ergo
BuildRequires : rubygem-indexer
BuildRequires : rubygem-lemon
BuildRequires : rubygem-mast
BuildRequires : rubygem-qed
BuildRequires : rubygem-rdoc

%description
# ANSI
[HOME](http://rubyworks.github.com/ansi) &middot;
[API](http://rubydoc.info/gems/ansi/frames) &middot;
[MAIL](http://googlegroups.com/group/rubyworks-mailinglist)  &middot;
[ISSUES](http://github.com/rubyworks/ansi/issues) &middot;
[SOURCE](http://github.com/rubyworks/ansi)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ansi-1.5.0
gem spec %{SOURCE0} -l --ruby > rubygem-ansi.gemspec

%build
gem build rubygem-ansi.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
ansi-1.5.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/ansi-1.5.0 && rubytest -I.:lib:test test/case_*.rb && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/ansi-1.5.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/.index
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/DEMO.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/NOTICE.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/01_ansicode.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/02_core.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/03_logger.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/04_progressbar.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/05_mixin.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/06_string.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/07_columns.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/08_table.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/09_diff.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/10_bbcode.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/11_terminal.md
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/applique/ae.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/demo/applique/output.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi.yml
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/bbcode.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/chain.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/chart.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/code.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/columns.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/constants.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/core.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/diff.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/hexdump.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/logger.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/progressbar.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/string.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/table.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/terminal.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/terminal/curses.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/terminal/stty.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/terminal/termios.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/terminal/win32.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/lib/ansi/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/test/case_ansicode.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/test/case_bbcode.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/test/case_mixin.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/test/case_progressbar.rb
/usr/lib64/ruby/gems/2.3.0/gems/ansi-1.5.0/test/test_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/ansi-1.5.0.gemspec
