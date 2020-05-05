# SimpleOP

这是一个可以在你自己的Minecraft服务器中在服务端进行``OP权限获取``、``重启服务器``、``关闭服务器``的插件，需配合[MCDReforged](https://github.com/Fallen-Breath/MCDReforged)使用。推荐用在[镜像服](https://github.com/GamerNoTitle/MCDR-Mirror-Server)中使用~

感谢[@Fallen_Breath](https://github.com/Fallen-Breath)给我指出插件中的问题~

使用``!!op``来给你op权限（记得自己deop掉）

使用``!!restart``来重启服务器

使用``!!stop``来关闭服务器

重启和关闭服务器的时间可以自由设定，打开``simpleOP.py``文件，在最顶上有个``waiting_time``，将这个数字改成任意正整数即可，单位是秒

如果你不需要``!!stop``（避免熊孩子滥用），只需要将开头的`stop_enable=1`改成`0`即可！

---

This is a plugin which can help you get OP permission, restart your server, close your server in game. Just input the following contents. Remember, using [MCDReforged](https://github.com/Fallen-Breath/MCDReforged) is essentials. Recommand to be used in [Mirror Server](https://github.com/GamerNoTitle/MCDR-Mirror-Server)

Special thanks to [@Fallen_Breath](https://github.com/Fallen-Breath)

`!!op` give you op

`!!restart` restart the server

``!!stop`` stop the server

The time can be set at the variable ``waiting_time``, just edit the number behind the variable ``waiting_time`` in seconds.

If you want to disable ``!!stop`` command, you can change the `stop_enable=1` into `0`



