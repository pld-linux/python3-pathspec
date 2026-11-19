#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Utility library for gitignore style pattern matching of file paths
Summary(pl.UTF-8):	Biblioteka narzędzioawa do dopasowywania wzorców ścieżek plików w stylu gitignore
Name:		python3-pathspec
Version:	1.1.1
Release:	1
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pathspec/
Source0:	https://pypi.debian.net/pathspec/pathspec-%{version}.tar.gz
# Source0-md5:	c762d0a00d6cfc9de003e02d5072b26a
URL:		https://pypi.org/project/pathspec/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-flit_core < 5
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
%if %{with tests}
# TODO: 9
BuildRequires:	python3-pytest >= 8.4
BuildRequires:	python3-typing_extensions >= 4.15
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
# TODO: 9.1.0
BuildRequires:	sphinx-pdg-3 >= 8.3
%endif
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pathspec is a utility library for pattern matching of file paths. So
far this only includes Git's wildmatch pattern matching which itself
is derived from Rsync's wildmatch. Git uses wildmatch for its
gitignore files.

%description -l pl.UTF-8
pathspec to biblioteka narzędziowa do dopasowywania wzorców ścieżek
plików. Obecnie obejmuje to tylko algorytm dopasowywania wildmatch
Gita, wywodzący się z wildmatch programu Rsync. Git wykorzystuje
wildmatch na potrzeby plików gitignore.

%package apidocs
Summary:	API documentation for Python pathspec module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pathspec
Group:		Documentation

%description apidocs
API documentation for Python pathspec module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pathspec.

%prep
%setup -q -n pathspec-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst README.rst UPGRADING.rst
%{py3_sitescriptdir}/pathspec
%{py3_sitescriptdir}/pathspec-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_modules,_static,*.html,*.js}
%endif
