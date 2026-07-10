File "/mount/src/dasbor-presensi/app.py", line 76, in <module>
    buat_halaman_aman("pages/1_Input_MKL.py", "📝  Input MKL")
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/mount/src/dasbor-presensi/app.py", line 72, in buat_halaman_aman
    st.page_link(path, label=label, use_container_width=True)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/runtime/metrics_util.py", line 568, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/widgets/button.py", line 1297, in page_link
    return self._page_link(
           ~~~~~~~~~~~~~~~^
        page=page,
        ^^^^^^^^^^
    ...<6 lines>...
        query_params=query_params,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
File "/home/adminuser/venv/lib/python3.14/site-packages/streamlit/elements/widgets/button.py", line 1601, in _page_link
    url_pathname = page_data["url_pathname"]
                   ~~~~~~~~~^^^^^^^^^^^^^^^^
