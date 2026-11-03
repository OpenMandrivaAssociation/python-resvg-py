%undefine _debugsource_packages

# Recreate the vendor archive after a version bump:
#   tar xf resvg_py-VERSION.tar.gz && cd resvg_py-VERSION
#   cargo vendor --locked vendor
#   tar cJf python-resvg-py-VERSION-vendor.tar.xz vendor
#   abb store python-resvg-py-VERSION-vendor.tar.xz

Name:		python-resvg-py
Version:	0.5.0
Release:	1
Summary:	Render SVG documents to PNG with resvg
License:	MIT
Group:		Development/Python
URL:		https://github.com/baseplate-admin/resvg-py
Source0:	https://files.pythonhosted.org/packages/source/r/resvg-py/resvg_py-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}-%{version}-vendor.tar.xz
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	cargo
BuildRequires:	rust-packaging

%description
resvg-py renders an SVG document to PNG bytes. The distribution name
is resvg-py; the import name is resvg_py. Hermes uses it when
generating icons. This build uses the bundled resvg 0.48 crate, which
is newer than the resvg 0.47 command-line package.

%prep -a
tar -xf %{SOURCE1}
%cargo_prep -v vendor

%build -p
export CARGO_HOME=$PWD/.cargo
export CARGO_NET_OFFLINE=true

%build -a
%cargo_license_summary
%{cargo_license} > LICENSES.dependencies

%files
%doc README.md
%license LICENSE LICENSES.dependencies
%{python_sitearch}/resvg_py
%{python_sitearch}/resvg_py-%{version}.dist-info
