import subprocess

def test_main():
    # make venv
    # install local package and pyright
    # run coverage, check it fails
    # run coverage with lower minimum, check it passes
    # check the same with --outputjson
    # check some extra argument too?
    subprocess.run(['uv', 'venv', 'tests/.venv'])
    subprocess.run(['uv', 'pip', 'install', '-U', 'pyright', '-e', 'tests/tmp-repo'])
    subprocess.run(['uv', 'pip', 'install', '-e', '.'])
    result = subprocess.run(['pyright-cov', '--verifytypes', 'foo', '--ignoreexternal'])
    assert result.returncode == 1
    result = subprocess.run(['pyright-cov', '--verifytypes', 'foo', '--ignoreexternal', '--outputjson'])
    assert result.returncode == 1
    result = subprocess.run(['pyright-cov', '--verifytypes', 'foo', '--ignoreexternal', '--fail-under', '60', '--exclude-like', '*.tests.*'])
    assert result.returncode == 0
    result = subprocess.run(['pyright-cov', '--verifytypes', 'foo', '--ignoreexternal', '--fail-under', '60', '--outputjson', '--exclude-like', '*.tests.*'])
    assert result.returncode == 0

