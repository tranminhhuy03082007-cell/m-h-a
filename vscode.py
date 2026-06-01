<?xml version="1.0" encoding="UTF-8"?>
<flowchart>
    <start id="1">START</start>

    <input id="2">
        <text>Nhập mã sách</text>
    </input>

    <decision id="3">
        <question>Mã sách rỗng?</question>
    </decision>

    <process id="4">
        <text>Thông báo lỗi</text>
    </process>

    <process id="5">
        <text>Kiểm tra mã sách</text>
    </process>

    <decision id="6">
        <question>Mã sách đã tồn tại?</question>
    </decision>

    <process id="7">
        <text>Thông báo đã tồn tại</text>
    </process>

    <input id="8">
        <text>Nhập tên sách và tác giả</text>
    </input>

    <decision id="9">
        <question>Tên sách hoặc tác giả rỗng?</question>
    </decision>

    <process id="10">
        <text>Thông báo lỗi</text>
    </process>

    <input id="11">
        <text>Nhập năm xuất bản và số lượng</text>
    </input>

    <decision id="12">
        <question>Dữ liệu là số?</question>
    </decision>

    <process id="13">
        <text>Thông báo lỗi</text>
    </process>

    <decision id="14">
        <question>Năm XB &gt; 0 và Số lượng &gt; 0 ?</question>
    </decision>

    <process id="15">
        <text>Thông báo lỗi</text>
    </process>

    <process id="16">
        <text>Tạo đối tượng sách</text>
    </process>

    <process id="17">
        <text>Thêm vào danh sách sách</text>
    </process>

    <output id="18">
        <text>Thông báo thành công</text>
    </output>

    <end id="19">END</end>
</flowchart>
