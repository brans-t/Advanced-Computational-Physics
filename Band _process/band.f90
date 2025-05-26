    !声明变量
    module global
      implicit none
      real, allocatable :: ev(:,:)    !二维可变数组，存储本征值
      real, allocatable :: kp(:,:)    !二维可变数组
      real, dimension(3) ::k_0,d      
      character(len=32) :: line, filename = "EIGENVAL"
      integer :: i, n, j
      real :: dk
      logical alive
    end module
    !主程序
    program band
    use global
    !查询是否存在EIGENVAL文件
    inquire(file=filename,exist=alive)
    if(alive)then
        write(*,*)"The required documents are ready!"
    else
        write(*,*)filename,"doesn't exist."
    end if
    !读取EIGNVAL文件，并创建band.dat文件
    open(unit = 10, file = 'EIGENVAL', status = 'old')
    open(unit = 11,file = 'band.dat')
    !通过循环，将前五行的数据读取并舍弃
    do n = 1,5
        read(10,'(A)') line
    end do
    
    !读取能带的k点以及对应的本征值
    read(10,*) none,nkp,nbands  
    !write(*,*) nkp, nbands
    allocate(ev(nkp,nbands))   !为数组ev分配内存空间，使其大小为（nkp,nbands）
    allocate(kp(nkp,3))        !为数组kp分配内存空间，使其大小为（nkp,3）
        do i = 1,nkp
            read(10,*)         !读取空行并舍弃
            read(10,*) (kp(i,j),j = 1,3),weight  !将第i个k点的三个坐标存储到kp中，权重存储到weight中
            do j = 1,nbands
                read(10,*) m,ev(i,j)   !将序号以及本征值存储在变量m和ev(i,j)中
            end do
        end do
!计算能带的波矢之间的距离
    do j = 1,nbands                  !遍历每个能带
        dk = 0                       !将变量dk初始化为0
        do i = 1,nkp                 
            if (i.eq.1) then        
                k_0 = kp(i,:)        !初始化变量k_0
            end if
            d = kp(i,:) - k_0        !计算当前波矢k(i,:)与前一个波矢k_0之间的差值，并将结果存储到数组b中
            dk = dk + sqrt(dot_product(d,d))  !计算当前波矢k(i,:)与前一个波矢k_0之间的距离，并累加到变量dk中。这里使用了向量的点积来计算距离
                write(11,*)dk,ev(i,j)  !将dk以及对应的本征值输出到band.dat文件中
            k_0 = kp(i,:)             !更新变量k_0
        end do
        write(11,*)
    end do
    write(*,*) "File output successful!"
    stop
    end program band