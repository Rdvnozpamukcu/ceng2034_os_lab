#!/bin/bash
mkdir /boot/grml
echo 'menuentry "Install on sdb1" {
    set root=(hd1,1)
    linux /vmlinuz root=/dev/sdb1 ro quiet splash
    initrd /initrd.img
}
' >> /etc/grub.d/40_custom
mv ~/<filename.iso> /boot/grml/
update-grub
