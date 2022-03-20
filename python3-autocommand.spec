#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	template
Summary:	Library to create a command-line program from a function
Summary(pl.UTF-8):	Biblioteka do tworzenia programów linii poleceń z funkcji
Name:		python3-autocommand
Version:	2.2.1
Release:	1
License:	LGPL v3
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/autocommand/
Source0:	https://files.pythonhosted.org/packages/source/a/autocommand/autocommand-%{version}.tar.gz
# Source0-md5:	0695be9e3b7de1e589ee4cbf3734ad3d
Patch0:		%{name}-async.patch
URL:		https://pypi.org/project/autocommand/
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to automatically generate and run simple argparse parsers
from function signatures.

%description -l pl.UTF-8
Biblioteka do automatycznego generowania i uruchamiania prostych
parserów argparse z sygnatur funkcji.

%prep
%setup -q -n autocommand-%{version}
%patch0 -p1

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/autocommand
%{py3_sitescriptdir}/autocommand-%{version}-py*.egg-info
