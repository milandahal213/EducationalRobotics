#http://javl.github.io/image2cpp/

BasicFont = [[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x00, 0x5F, 0x00, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x00, 0x07, 0x00, 0x07, 0x00, 0x00, 0x00],
             [0x00, 0x14, 0x7F, 0x14, 0x7F, 0x14, 0x00, 0x00],
             [0x00, 0x24, 0x2A, 0x7F, 0x2A, 0x12, 0x00, 0x00],
             [0x00, 0x23, 0x13, 0x08, 0x64, 0x62, 0x00, 0x00],
             [0x00, 0x36, 0x49, 0x55, 0x22, 0x50, 0x00, 0x00],
             [0x00, 0x00, 0x05, 0x03, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x1C, 0x22, 0x41, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x41, 0x22, 0x1C, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x08, 0x2A, 0x1C, 0x2A, 0x08, 0x00, 0x00],
             [0x00, 0x08, 0x08, 0x3E, 0x08, 0x08, 0x00, 0x00],
             [0x00, 0xA0, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x08, 0x08, 0x08, 0x08, 0x08, 0x00, 0x00],
             [0x00, 0x60, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x20, 0x10, 0x08, 0x04, 0x02, 0x00, 0x00],
             [0x00, 0x3E, 0x51, 0x49, 0x45, 0x3E, 0x00, 0x00],
             [0x00, 0x00, 0x42, 0x7F, 0x40, 0x00, 0x00, 0x00],
             [0x00, 0x62, 0x51, 0x49, 0x49, 0x46, 0x00, 0x00],
             [0x00, 0x22, 0x41, 0x49, 0x49, 0x36, 0x00, 0x00],
             [0x00, 0x18, 0x14, 0x12, 0x7F, 0x10, 0x00, 0x00],
             [0x00, 0x27, 0x45, 0x45, 0x45, 0x39, 0x00, 0x00],
             [0x00, 0x3C, 0x4A, 0x49, 0x49, 0x30, 0x00, 0x00],
             [0x00, 0x01, 0x71, 0x09, 0x05, 0x03, 0x00, 0x00],
             [0x00, 0x36, 0x49, 0x49, 0x49, 0x36, 0x00, 0x00],
             [0x00, 0x06, 0x49, 0x49, 0x29, 0x1E, 0x00, 0x00],
             [0x00, 0x00, 0x36, 0x36, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x00, 0xAC, 0x6C, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x08, 0x14, 0x22, 0x41, 0x00, 0x00, 0x00],
             [0x00, 0x14, 0x14, 0x14, 0x14, 0x14, 0x00, 0x00],
             [0x00, 0x41, 0x22, 0x14, 0x08, 0x00, 0x00, 0x00],
             [0x00, 0x02, 0x01, 0x51, 0x09, 0x06, 0x00, 0x00],
             [0x00, 0x32, 0x49, 0x79, 0x41, 0x3E, 0x00, 0x00],
             [0x00, 0x7E, 0x09, 0x09, 0x09, 0x7E, 0x00, 0x00],
             [0x00, 0x7F, 0x49, 0x49, 0x49, 0x36, 0x00, 0x00],
             [0x00, 0x3E, 0x41, 0x41, 0x41, 0x22, 0x00, 0x00],
             [0x00, 0x7F, 0x41, 0x41, 0x22, 0x1C, 0x00, 0x00],
             [0x00, 0x7F, 0x49, 0x49, 0x49, 0x41, 0x00, 0x00],
             [0x00, 0x7F, 0x09, 0x09, 0x09, 0x01, 0x00, 0x00],
             [0x00, 0x3E, 0x41, 0x41, 0x51, 0x72, 0x00, 0x00],
             [0x00, 0x7F, 0x08, 0x08, 0x08, 0x7F, 0x00, 0x00],
             [0x00, 0x41, 0x7F, 0x41, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x20, 0x40, 0x41, 0x3F, 0x01, 0x00, 0x00],
             [0x00, 0x7F, 0x08, 0x14, 0x22, 0x41, 0x00, 0x00],
             [0x00, 0x7F, 0x40, 0x40, 0x40, 0x40, 0x00, 0x00],
             [0x00, 0x7F, 0x02, 0x0C, 0x02, 0x7F, 0x00, 0x00],
             [0x00, 0x7F, 0x04, 0x08, 0x10, 0x7F, 0x00, 0x00],
             [0x00, 0x3E, 0x41, 0x41, 0x41, 0x3E, 0x00, 0x00],
             [0x00, 0x7F, 0x09, 0x09, 0x09, 0x06, 0x00, 0x00],
             [0x00, 0x3E, 0x41, 0x51, 0x21, 0x5E, 0x00, 0x00],
             [0x00, 0x7F, 0x09, 0x19, 0x29, 0x46, 0x00, 0x00],
             [0x00, 0x26, 0x49, 0x49, 0x49, 0x32, 0x00, 0x00],
             [0x00, 0x01, 0x01, 0x7F, 0x01, 0x01, 0x00, 0x00],
             [0x00, 0x3F, 0x40, 0x40, 0x40, 0x3F, 0x00, 0x00],
             [0x00, 0x1F, 0x20, 0x40, 0x20, 0x1F, 0x00, 0x00],
             [0x00, 0x3F, 0x40, 0x38, 0x40, 0x3F, 0x00, 0x00],
             [0x00, 0x63, 0x14, 0x08, 0x14, 0x63, 0x00, 0x00],
             [0x00, 0x03, 0x04, 0x78, 0x04, 0x03, 0x00, 0x00],
             [0x00, 0x61, 0x51, 0x49, 0x45, 0x43, 0x00, 0x00],
             [0x00, 0x7F, 0x41, 0x41, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x02, 0x04, 0x08, 0x10, 0x20, 0x00, 0x00],
             [0x00, 0x41, 0x41, 0x7F, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x04, 0x02, 0x01, 0x02, 0x04, 0x00, 0x00],
             [0x00, 0x80, 0x80, 0x80, 0x80, 0x80, 0x00, 0x00],
             [0x00, 0x01, 0x02, 0x04, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x20, 0x54, 0x54, 0x54, 0x78, 0x00, 0x00],
             [0x00, 0x7F, 0x48, 0x44, 0x44, 0x38, 0x00, 0x00],
             [0x00, 0x38, 0x44, 0x44, 0x28, 0x00, 0x00, 0x00],
             [0x00, 0x38, 0x44, 0x44, 0x48, 0x7F, 0x00, 0x00],
             [0x00, 0x38, 0x54, 0x54, 0x54, 0x18, 0x00, 0x00],
             [0x00, 0x08, 0x7E, 0x09, 0x02, 0x00, 0x00, 0x00],
             [0x00, 0x18, 0xA4, 0xA4, 0xA4, 0x7C, 0x00, 0x00],
             [0x00, 0x7F, 0x08, 0x04, 0x04, 0x78, 0x00, 0x00],
             [0x00, 0x00, 0x7D, 0x00, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x80, 0x84, 0x7D, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x7F, 0x10, 0x28, 0x44, 0x00, 0x00, 0x00],
             [0x00, 0x41, 0x7F, 0x40, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x7C, 0x04, 0x18, 0x04, 0x78, 0x00, 0x00],
             [0x00, 0x7C, 0x08, 0x04, 0x7C, 0x00, 0x00, 0x00],
             [0x00, 0x38, 0x44, 0x44, 0x38, 0x00, 0x00, 0x00],
             [0x00, 0xFC, 0x24, 0x24, 0x18, 0x00, 0x00, 0x00],
             [0x00, 0x18, 0x24, 0x24, 0xFC, 0x00, 0x00, 0x00],
             [0x00, 0x00, 0x7C, 0x08, 0x04, 0x00, 0x00, 0x00],
             [0x00, 0x48, 0x54, 0x54, 0x24, 0x00, 0x00, 0x00],
             [0x00, 0x04, 0x7F, 0x44, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x3C, 0x40, 0x40, 0x7C, 0x00, 0x00, 0x00],
             [0x00, 0x1C, 0x20, 0x40, 0x20, 0x1C, 0x00, 0x00],
             [0x00, 0x3C, 0x40, 0x30, 0x40, 0x3C, 0x00, 0x00],
             [0x00, 0x44, 0x28, 0x10, 0x28, 0x44, 0x00, 0x00],
             [0x00, 0x1C, 0xA0, 0xA0, 0x7C, 0x00, 0x00, 0x00],
             [0x00, 0x44, 0x64, 0x54, 0x4C, 0x44, 0x00, 0x00],
             [0x00, 0x08, 0x36, 0x41, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x00, 0x7F, 0x00, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x41, 0x36, 0x08, 0x00, 0x00, 0x00, 0x00],
             [0x00, 0x02, 0x01, 0x01, 0x02, 0x01, 0x00, 0x00],
             [0x00, 0x02, 0x05, 0x05, 0x02, 0x00, 0x00, 0x00]]


SeeedLogo=[
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x80,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
0x60, 0xf0, 0xc0, 0x00, 0x00, 0x00, 0xfc, 0xff, 0x87, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x03,
0xff, 0xfc, 0x00, 0x00, 0x00, 0x80, 0xf0, 0x20, 0x00, 0x00, 0x80,0xc0, 0xc0, 0x60, 0xe0, 0xc0,
0xc0, 0x00, 0x00, 0x00, 0xc0, 0xc0, 0xc0, 0x60, 0xe0, 0xc0, 0xc0,0x80, 0x00, 0x00, 0x80, 0xc0,
0xc0, 0xe0, 0x60, 0xc0, 0xc0, 0x80, 0x00, 0x00, 0x00, 0xc0, 0xc0,0xc0, 0x60, 0xe0, 0xc0, 0xc0,
0x80, 0x00, 0x00, 0x80, 0xc0, 0xc0, 0xe0, 0xe0, 0xc0, 0xc0, 0xf8,0xf8, 0x00, 0x00, 0x00, 0x00,
0x00, 0xc0, 0xc0, 0xe0, 0x60, 0xc0, 0xc0, 0x80, 0x00, 0xc0, 0xf0,0xf0, 0xf0, 0xc0, 0x00, 0xc0,
0xc0, 0x00, 0x00, 0x00, 0x00, 0xc0, 0xc0, 0x00, 0x00, 0x80, 0xc0,0xc0, 0xe0, 0xe0, 0xc0, 0xc0,
0xf8, 0xf8, 0x00, 0xd8, 0xd8, 0x00, 0x00, 0x80, 0xc0, 0xc0, 0xe0,0x60, 0xc0, 0xc0, 0x80, 0x00,
0x00, 0x03, 0x0f, 0x1e, 0x3c, 0x70, 0xe3, 0xcf, 0x9f, 0x30, 0x00,0x00, 0x00, 0x00, 0x70, 0xbf,
0xcf, 0xe3, 0x70, 0x78, 0x3e, 0x0f, 0x03, 0x00, 0x00, 0x00, 0x33,0x77, 0x66, 0x66, 0x66, 0x6c,
0x7d, 0x18, 0x00, 0x1f, 0x3f, 0x76, 0x66, 0x66, 0x66, 0x76, 0x37,0x07, 0x00, 0x0f, 0x3f, 0x7f,
0x66, 0x66, 0x66, 0x66, 0x77, 0x27, 0x07, 0x00, 0x1f, 0x3f, 0x76,0x66, 0x66, 0x66, 0x76, 0x37,
0x07, 0x00, 0x0f, 0x3f, 0x71, 0x60, 0x60, 0x60, 0x60, 0x31, 0x7f, 0x7f, 0x00, 0x00, 0x00, 0x00,
0x11, 0x37, 0x67, 0x66, 0x66, 0x6c, 0x7d, 0x38, 0x00, 0x00, 0x3f, 0x7f, 0x3f, 0x00, 0x00, 0x1f,
0x3f, 0x70, 0x60, 0x60, 0x70, 0x7f, 0x7f, 0x00, 0x0f, 0x3f, 0x71, 0x60, 0x60, 0x60, 0x60, 0x31,
0x7f, 0x7f, 0x00, 0x7f, 0x7f, 0x00, 0x06, 0x1f, 0x3b, 0x60, 0x60, 0x60, 0x60, 0x71, 0x3f, 0x1f,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01,
0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x48, 0x48, 0x48, 0xb0, 0x00, 0xc0, 0x20,
0x20, 0x20, 0xc0, 0x00, 0xc0, 0x20, 0x20, 0x20, 0xc0, 0x00, 0x40, 0xa0, 0xa0, 0xa0, 0x20, 0x00,
0x00, 0x20, 0xf0, 0x20, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0x08, 0xf8, 0x08,
0x08, 0x00, 0xc0, 0x20, 0x20, 0x20, 0xf8, 0x00, 0xc0, 0xa0, 0xa0, 0xa0, 0xc0, 0x00, 0x20, 0xa0,
0xa0, 0xa0, 0xc0, 0x00, 0x40, 0xa0, 0xa0, 0xa0, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xf8, 0x48, 0x48, 0x48, 0x08, 0x00, 0x20, 0x40, 0x80, 0x40,
0x20, 0x00, 0x00, 0x20, 0xf0, 0x20, 0x20, 0x00, 0xc0, 0xa0, 0xa0, 0xa0, 0xc0, 0x00, 0xe0, 0x00,
0x20, 0x20, 0xc0, 0x00, 0xc0, 0x20, 0x20, 0x20, 0xf8, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x02, 0x02, 0x02, 0x01, 0x00, 0x01, 0x02,
0x02, 0x02, 0x01, 0x00, 0x01, 0x02, 0x02, 0x02, 0x01, 0x00, 0x02, 0x02, 0x02, 0x02, 0x01, 0x00,
0x00, 0x00, 0x01, 0x02, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0x02, 0x03, 0x02,
0x02, 0x00, 0x01, 0x02, 0x02, 0x02, 0x03, 0x00, 0x01, 0x02, 0x02, 0x02, 0x00, 0x00, 0x01, 0x02,
0x02, 0x02, 0x01, 0x02, 0x02, 0x02, 0x02, 0x02, 0x01, 0x00, 0x00, 0x08, 0x06, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x02, 0x02, 0x82, 0x02, 0x00, 0x02, 0x01, 0x01, 0x01,
0x02, 0x00, 0x00, 0x00, 0x01, 0x02, 0x02, 0x00, 0x01, 0x02, 0x02, 0x02, 0x00, 0x00, 0x03, 0x00,
0x00, 0x00, 0x03, 0x00, 0x01, 0x02, 0x02, 0x02, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x82, 0x8c, 0x60, 0x1c, 0x02, 0x00, 0x1c, 0x22, 0x22, 0x22, 0x1c, 0x00, 0x1e,
0x20, 0x20, 0x00, 0x3e, 0x00, 0x00, 0x3e, 0x04, 0x02, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x3e, 0x04, 0x02, 0x02, 0x00, 0x1c, 0x2a, 0x2a, 0x2a, 0x0c, 0x00, 0x12, 0x2a, 0x2a,
0x2a, 0x1c, 0x20, 0x1c, 0x22, 0x22, 0x22, 0x14, 0x00, 0x3f, 0x00, 0x02, 0x02, 0x3c, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00,
   0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00, 0x00
 ]
eye=[ 0xff, 0x00, 0xff, 0x00, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x7f, 0x7f, 0x3f, 
	0x1f, 0x1f, 0x0f, 0x0f, 0x87, 0x87, 0x87, 0xc3, 0xc3, 0xc3, 0xe3, 0xe1, 0xe1, 0xe1, 0xe1, 0xe1, 
	0xe1, 0xe1, 0xe1, 0xe1, 0xe1, 0xe3, 0xe3, 0xc3, 0xc3, 0xc7, 0x87, 0x87, 0x0f, 0x0f, 0x1f, 0x1f, 
	0x3f, 0x3f, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x7f, 0x3f, 0x0f, 0x07, 0x03, 0xc1, 0xe0, 0xf0, 0xf8, 0xf8, 
	0xfc, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0xfe, 
	0xfc, 0xf8, 0xf0, 0xe0, 0xc1, 0x83, 0x07, 0x0f, 0x1f, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0x1f, 0x07, 0x01, 0x80, 0xe0, 0xf8, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0x7f, 0x3f, 0x3f, 0x1f, 0x1f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x1f, 0x1f, 
	0x1f, 0x3f, 0x7f, 0xff, 0xff, 0xff, 0xff, 0xfc, 0xf0, 0xc0, 0x00, 0x03, 0x0f, 0x3f, 0xff, 0xff, 
	0xff, 0x1f, 0x00, 0x00, 0x00, 0xfc, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x1f, 
	0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3c, 0x7e, 0x7e, 
	0x7e, 0x7e, 0x3c, 0x00, 0x01, 0x07, 0xff, 0xff, 0xff, 0xff, 0xfe, 0xc0, 0x00, 0x00, 0x03, 0xff, 
	0xff, 0xf0, 0x00, 0x00, 0x00, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xf8, 
	0xc0, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
	0x00, 0x00, 0x00, 0x00, 0xc0, 0xe0, 0xff, 0xff, 0xff, 0xff, 0xff, 0x07, 0x00, 0x00, 0x80, 0xff, 
	0xff, 0xff, 0xfe, 0xf0, 0xc0, 0x00, 0x03, 0x0f, 0x3f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xfe, 0xfc, 0xfc, 0xf8, 0xf8, 0xf8, 0xf0, 0xf0, 0xf0, 0xf0, 0xf8, 0xf8, 0xf8, 
	0xfc, 0xfc, 0xfe, 0xff, 0xff, 0xff, 0xff, 0x7f, 0x1f, 0x07, 0x00, 0x80, 0xe0, 0xf8, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfc, 0xf8, 0xe0, 0xc0, 0x81, 0x03, 0x0f, 0x1f, 0x3f, 0x3f, 
	0x7f, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x7f, 
	0x7f, 0x3f, 0x1f, 0x0f, 0x07, 0x83, 0xc1, 0xe0, 0xf0, 0xf8, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 
	0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xfe, 0xfe, 0xfc, 0xf8, 
	0xf8, 0xf0, 0xe0, 0xe1, 0xe3, 0xc3, 0xc3, 0x87, 0x87, 0x87, 0x8f, 0x8f, 0x0f, 0x0f, 0x0f, 0x0f, 
	0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x8f, 0x87, 0x87, 0x87, 0xc7, 0xc3, 0xc3, 0xe1, 0xe1, 0xf0, 0xf0, 
	0xf8, 0xfc, 0xfc, 0xfe, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff]


eyeball=[
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,   0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,   
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0xff,0xff,0xff,0xff,0xff,0xff,0xff,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,   0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,   
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,   0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00, 0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,  0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
]


