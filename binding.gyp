{
    "targets": [
        {
            "target_name": "hello",
            "sources": [ "src/hello.cc" ]
        },{
            "target_name": "mesh",
            'include_dirs': [
                "library/eigenlib",
                "library/vcglib"
            ],
            "sources": [
                "src/mesh/mesh.cc",
                "src/mesh/myobject.cc"
            ],
            "cflags_cc!": [
                "-std=c++11",
                "-fno-exceptions",
                "-frtti"
            ],
            'conditions': [
                ['OS=="mac"', {
                    'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                        'GCC_ENABLE_CPP_RTTI': 'YES'
                    }
                }]
            ]
        }
    ],
}